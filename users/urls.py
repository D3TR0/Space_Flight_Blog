from django.urls import path
from users import views

app_name = 'blog'
urlpatterns=[
    path('register/', views.register, name='register'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate')
]