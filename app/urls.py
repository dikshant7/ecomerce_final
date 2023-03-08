from django.conf import settings
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.home),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
     path('laptop/', views.laptop, name='laptop'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('topwear/', views.topwear, name='topwear'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('logout/', views.logout, name='logout'),
    path('remove/',views.add_to_cart1,name='add-to-cart1'),
    path('add/',views.add_to_cart2,name='add-to-cart2'),
    path('decrease/',views.add_to_cart3,name='add-to-cart3'),
    path('order_placed/',views.order_placed,name='order_placed'),
    path('buyadd',views.buyadd,name='buyadd'),
    path('buysub',views.buysub,name='buysub'),
    path('checkoutbuynow',views.checkoutbuynow,name='checkoutbuynow'),
    path('order_placed_buy_now',views.order_placed_buy_now,name='order_placed_buy_now'),
] 
urlpatterns+=staticfiles_urlpatterns()
