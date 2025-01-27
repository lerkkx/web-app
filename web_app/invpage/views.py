from django.shortcuts import render, redirect, get_object_or_404
from .models import InventoryRequest, InventoryItem, Ownership
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def create_request(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        InventoryRequest.objects.create(user=request.user, item_name=item_name)
        return redirect('track_requests')
    

    inventory_items = InventoryItem.objects.all()  
    return render(request, 'invpage/index.html', {'user_info': request.user, 'inventory_items': inventory_items})

@login_required
def track_requests(request):
    requests = InventoryRequest.objects.filter(user=request.user)
    return render(request, 'invpage/track_requests.html', {'requests': requests})

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def manage_requests(request):
    
    pending_requests = InventoryRequest.objects.filter(status='В ожидании')
    
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        action = request.POST.get('action') 
        
        user = request.user
        inventory_request = get_object_or_404(InventoryRequest, request_id=request_id)
        
        
        if action == 'approve':
            inventory_request.status = 'Заявка одобрена'
            item_id = InventoryItem.objects.get(name=inventory_request.item_name)
            if Ownership.objects.filter(user=user, item=item_id).exists():
                items = Ownership.objects.get(user=user, item=item_id)
                items.quantity+=1
                items.save()
            else:
                Ownership.objects.create(
                    user=inventory_request.user,
                    item=InventoryItem.objects.get(name=inventory_request.item_name),
                    quantity=inventory_request.quantity)
            
        elif action == 'reject':
            inventory_request.status = 'Заявка отклонена'
        
        
        inventory_request.save()
        

        return redirect('manage_requests')
    

    return render(request, 'invpage/request_direct.html', {'pending_requests': pending_requests})

@login_required
def owned_inv(request):
    user = request.user
    
    owned_items = Ownership.objects.filter(user=user).select_related('item')
    
    return render(request, 'inventory_owned.html', {'owned_items': owned_items})