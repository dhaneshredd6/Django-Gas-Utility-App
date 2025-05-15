from django.contrib import admin
from django.urls import path, include
from services.views import user_dashboard
from services import views  # ✅ Correct import from the app where your views are defined

from django.contrib.auth import views as auth_views  # ✅ This fixes the "auth_views not defined" error
from django.contrib.admin.views.decorators import staff_member_required



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_dashboard, name='home'),  # dashboard as homepage
    # path('', include('services.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', include('services.urls')), 
    path('services/', include('services.urls')),
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff/approve/<int:pk>/', views.approve_request, name='approve_request'),
    path('staff/reject/<int:pk>/', views.reject_request, name='reject_request'),
    path('staff/bulk_resolve/', views.bulk_resolve, name='bulk_resolve'),

]
