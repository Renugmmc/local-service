from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group,User
from .models import Service
from .forms import RegisterForm

# Create your views here.
def home_view(request):
    return render(request,'index.html')

def service_view(request):
    return render(request,'service.html')

def aboutus_view(request):
    return render(request,'aboutus.html')

def login_view(request):
    return render(request,'login.html')

def contact_view(request):
    return render(request,'contact.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role')

            user = User.objects.create_user(username=username,email=email,password=password)
            user.is_staff = True
            user.save()

            group = Group.objects.get(name=request.POST['role'])
            user.groups.add(group)
            return redirect('/admin/login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
    
def table_view(request):
    return render(request,'table.html')

def blog_view(request):
    return render(request,'blog.html')