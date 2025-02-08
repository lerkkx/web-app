from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def create_request(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))
        item_quantity = InventoryItem.objects.get(item_id=item_id).quantity

        sum1 = quantity
        for i in InventoryRequest.objects.filter(item_id=item_id, status='В ожидании'):
            print(sum1)
            sum1 += i.quantity
        for i in InventoryRequest.objects.filter(item_id=item_id, status='В ожидании'):
            i.quantity_of_all = sum1
            i.save()
        
        InventoryRequest.objects.create(user=request.user, item_name=item_name, quantity = quantity, item_id=item_id, quantity_of_all=sum1, quantity_item=item_quantity)
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
        action1 = request.POST.get('action1') 
        inventory_request = get_object_or_404(InventoryRequest, request_id=request_id)
        
        if action == 'approve':
            inventory_request.status = 'Заявка одобрена'
            
            try:
                item = InventoryItem.objects.get(item_id=inventory_request.item_id)
                
                if item.quantity >= inventory_request.quantity:
                    item.quantity -= inventory_request.quantity  
                    item.save()
                    
                    ownership, created = Ownership.objects.get_or_create(
                        user=inventory_request.user,
                        item=item,
                        defaults={'quantity': 0}
                    )
                    ownership.quantity += inventory_request.quantity
                    ownership.save()
                else:
                    print("Недостаточно предметов в наличии.")
            except InventoryItem.DoesNotExist:
                print("Предмет не найден.")
        elif action1 == 'continue_w':
            
            item = InventoryItem.objects.get(item_id=inventory_request.item_id)
            inventory_request.status = "Заявка одобрена"
            for i in InventoryRequest.objects.filter(item_id=inventory_request.item_id , status="В ожидании"):
                i.status = 'Заявка отклонена'
                i.save()
            item.quantity -= inventory_request.quantity  
            item.save()
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

@login_required
def reports_view(request):
    inventory_requests = InventoryRequest.objects.all()
    inventory_items = InventoryItem.objects.all()
    ownerships = Ownership.objects.all()
    purchase_plans = PurchasePlan.objects.all()
    usage_reports = UsageReport.objects.all()

    context = {
        'inventory_requests': inventory_requests,
        'inventory_items': inventory_items,
        'ownerships': ownerships,
        'purchase_plans': purchase_plans,
        'usage_reports': usage_reports,
    }
    return render(request, 'invpage/reports.html', context)
