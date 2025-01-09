from django.shortcuts import render, redirect

def index(request):
    
    user_id = request.user.id
    if user_id:
        print(user_id)
        return render(request, 'invpage/index.html', {'user_info': request.user})
    else:
    
        return redirect('user_login')