from django.urls import path
from . import views


app_name = 'catalog'
urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('product_detail/<int:pk>', views.product_detail, name='product_detail'),
    path('add_product', views.add_product, name='add_product')
]