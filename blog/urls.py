
from django.urls import path
from . import views
from .views import ServiciosListView

urlpatterns = [
    path('', views.post_list, name='inicio'), 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    

    # Servicios

    path('servicios/', ServiciosListView.as_view(), name='servicios_list'),
    path('servicios/<int:pk>/', views.servicios_detail, name='servicios_detail'),
    path('servicios/new', views.servicios_new, name='servicios_new'),
    path('servicios/<int:pk>/edit/', views.servicios_edit, name='servicios_edit'),


    path('busqueda/', views.busqueda, name='Busqueda'),
    path('buscar/', views.buscar),
]