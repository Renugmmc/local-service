from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request,'register.html')
    
def table_view(request):
    return render(request,'table.html')

def blog_view(request):
    return render(request,'blog.html')