"""Projekt_Blog_WWW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
import users
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('', include('blog.urls', namespace='blog')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    #path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login', users.views.custom_login, name='login'),
    path('logout', users.views.custom_logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/', views.passwordResetConfirm, name='password_reset_confirm'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)