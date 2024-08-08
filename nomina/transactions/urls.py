from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('transaction/new/', views.transaction_create, name='transaction_create'),
    path('transaction/<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('transaction/<int:pk>/edit/', views.transaction_update, name='transaction_update'),
    path('transaction/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
]
