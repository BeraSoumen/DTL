from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')

def login_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
            
    return render(request, 'login.html')