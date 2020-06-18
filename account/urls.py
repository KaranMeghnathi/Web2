from django.urls import path
from . import views

urlpatterns =[
    path('Rform', views.Rform, name="Rform"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
