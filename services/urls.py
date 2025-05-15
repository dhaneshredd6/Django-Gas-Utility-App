from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
   
     path('', views.user_dashboard, name='home'),
     path('register/', views.register, name='register'),
    path('submit/', views.submit_request, name='submit_request'),
    path('requests/', views.request_list, name='request_list'),
    path('login/', auth_views.LoginView.as_view(template_name='services/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff/approve/<int:pk>/', views.approve_request, name='approve_request'),
    path('staff/reject/<int:pk>/', views.reject_request, name='reject_request'),
    path('staff/bulk_resolve/', views.bulk_resolve, name='bulk_resolve'),
]
