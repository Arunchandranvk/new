from django.urls import path
from .views import *

urlpatterns = [
    path('login',LoginView.as_view(),name='log'),
    path('registration/',RegistrationStudentView.as_view(),name='reg_stu'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile-update/<int:pk>/',ProfileUpdateView.as_view(),name='update_profile'),
    path('product-create/',ProductCreateView.as_view(),name='product_add'),
    path('product-update/<int:pk>/',ProductUpdateView.as_view(),name='product_update'),
    path('product-delete/<int:pk>/',ProductDeleteView.as_view(),name='product_delete'),
    path('products-all/',ProductGetView.as_view(),name='pro'),
]