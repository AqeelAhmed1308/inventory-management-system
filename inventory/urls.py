from django.urls import path
from . import views

urlpatterns = [
    path('stores/', views.StoreList.as_view()),
    path('stores/<int:pk>/', views.StoreDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('staff/', views.StaffList.as_view()),
    path('staff/<int:pk>/', views.StaffDetail.as_view()),
    path('managers/', views.ManagerList.as_view()),
    path('managers/<int:pk>/', views.ManagerDetail.as_view()),
]
