from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='homepage'),
    path('about/', views.home,name='aboutpage'),
    path('search/',views.search,name = 'search'),
    path('add/',views.add_project,name = 'add_project'),
    
]