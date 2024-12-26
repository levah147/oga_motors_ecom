from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path("category/", views.category_list, name='category-list'),
    path("product/", views.product_list_view, name='product-list'),
]
