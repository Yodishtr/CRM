from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from core.views import index, about
from userprofile.views import signup, custom_logout, myaccount

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/clients/', include('client.urls')),
    path('dashboard/myacccount/', myaccount, name='myaccount'),
    path('dashboard/teams/', include('team.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('about/', about, name='about'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', custom_logout, name='logout'),
    path('admin/', admin.site.urls),

]
