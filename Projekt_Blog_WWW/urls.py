from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import users
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('', include('blog.urls', namespace='blog')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('login', users.views.custom_login, name='login'),
    path('logout', users.views.custom_logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/', views.passwordResetConfirm, name='password_reset_confirm'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)