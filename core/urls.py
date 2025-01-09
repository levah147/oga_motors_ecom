from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # home
    path('', views.index, name='index13'),
    path("product/", views.product_list_view, name='product-list'),

    # catygory
    path("category/", views.category_list, name='category-list'),
    path("category/<cid>", views.category_product_list, name='category_product_list'),
    
    # vendor
    path("vendor/", views.vendor_list_view, name='vendor_list'),
    path("vendor/<vid>", views.vendor_detail_view, name='vendor_detail_view'),

]
