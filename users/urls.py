from django.urls import path
from users import views

app_name = 'blog'
urlpatterns=[
    path('register/', views.register, name='register'),
    path('flight/', views.flight, name='flight'),
    path('flights_table/', views.flights_table, name='flights_table'),
]