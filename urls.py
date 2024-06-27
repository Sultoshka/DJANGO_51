from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from products.views import HomePage, product_page, search, add_product_to_cart, user_cart
# ИМПОРТ!!
from users.views import register_view, login_view, profile_view, logout_view

from django.urls import path
from .views import delete_product_from_cart



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('search', search),
    path('products/<int:id>', product_page),
    path('signup', register_view, name='signup'),
    path('login', login_view, name='login'),
    path('profile', profile_view, name='profile'),
    path('logout', logout_view, name='logout'),
    path('add_to_cart/<int:id>', add_product_to_cart),
    path('user_cart', user_cart),
    path('cart/<int:cart_id>/delete/<int:product_id>/', delete_product_from_cart, name='delete_product_from_cart'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
