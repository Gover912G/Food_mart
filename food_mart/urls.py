from django.urls import path
from . import views


app_name = "foodmart"
urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name = "contact"),
    path('about', views.about, name = 'about'),
    path('shop', views.shop, name = "shop"),
    path('single_product', views.singleProduct, name = "single-product"),
    path('cart', views.cart, name = "cart"),
    path('check_out', views.checkOut, name = "check-out"),
    path('blog', views.blog, name = "blog"),
    path('single_post', views.singlePost, name = "single-post"),
    path('styles', views.styles, name = "styles"),
    #path('thankyou', views.thankyou, name = "thankyou"),
    path('account', views.myaccount, name = "account"),
    #path('404', views.404, name = "404"),


]