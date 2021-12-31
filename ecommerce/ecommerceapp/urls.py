from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('all-latests-Products',views.allproducts,name="allproducts"),
    path('featured',views.featured,name="featured"),
    path('review',views.review,name="review"),
    path('view-product/<id>',views.viewproduct,name="viewproduct"),
    path('cart',views.cart,name="cart"),

    
]