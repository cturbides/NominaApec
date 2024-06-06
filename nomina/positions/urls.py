from django.urls import path

from . import views

urlpatterns = [
    path('', views.position_list, name='position_list'),
    path('position/new/', views.position_create, name='position_create'),
    path('position/<int:pk>/', views.position_detail, name='position_detail'),
    path('position/<int:pk>/edit/', views.position_update, name='position_update'),
    path('position/<int:pk>/delete/', views.position_delete, name='position_delete'),
]
