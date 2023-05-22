from django.urls import path

from .views import ProductListView, OrderSuccessView, PlaceOrderView

urlpatterns = [

    path('', ProductListView.as_view(), name='product-list-all'),
    path('add/', PlaceOrderView(), name='place-order'),
    path('add/', ProductListView(), name='product-list'),
    path('add/', OrderSuccessView(), name='order-success'),

]
