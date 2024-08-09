from . import views
from django.urls import path

urlpatterns = [
    path('', views.search, name='search'),
    path('get_options/', views.get_options, name='get_options'),
    path('search_results/', views.search_result, name='search_results'),
]
