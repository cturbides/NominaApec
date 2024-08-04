from django.urls import path
from . import views

urlpatterns = [
    path('', views.deduction_list, name='deduction_list'),
    path('deduction/<int:pk>/', views.deduction_detail, name='deduction_detail'),
    path('deduction/new/', views.deduction_create, name='deduction_create'),
    path('deduction/<int:pk>/edit/', views.deduction_update, name='deduction_update'),
    path('deduction/<int:pk>/delete/', views.deduction_delete, name='deduction_delete'),
]
