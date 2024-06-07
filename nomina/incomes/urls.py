from django.urls import path
from . import views

urlpatterns = [
    path('', views.income_list, name='income_list'),
    path('income/<int:pk>/', views.income_detail, name='income_detail'),
    path('income/new/', views.income_create, name='income_create'),
    path('income/<int:pk>/edit/', views.income_update, name='income_update'),
    path('income/<int:pk>/delete/', views.income_delete, name='income_delete'),
]
