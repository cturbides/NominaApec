from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('department/new/', views.department_create, name='department_create'),
    path('department/<int:pk>/edit/', views.department_update, name='department_update'),
    path('department/<int:pk>/delete/', views.department_delete, name='department_delete'),
]
