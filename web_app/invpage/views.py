from django.shortcuts import render, redirect
from .models import InventoryRequest, InventoryItem  
from django.contrib.auth.decorators import login_required

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
