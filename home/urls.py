# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('service/', views.service_view, name='service'),
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.contact_view, name='contact'),
    path('register/', views.register_view, name='register'),
    path('blog/', views.blog_view, name='blog'),
    path('table/', views.table_view, name='table'),
]
