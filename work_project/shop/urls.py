from django.urls import path

from .views import ProductListView, OrderSuccessView, PlaceOrderView

urlpatterns = [

    path('', ProductListView.as_view(), name='product-list-all'),
    path('add/', PlaceOrderView().as_view(), name='place-order'),
    path('add/', ProductListView().as_view(), name='product-list'),
    path('add/', OrderSuccessView().as_view(), name='order-success'),

]
