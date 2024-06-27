from django.contrib import admin
from .models import CartModel
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"


# Создаем таблицу для Категории
class CategoryModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


# Создаем таблицу для Продуктов
class ProductModel(models.Model):
    title = models.CharField(max_length=100, help_text='Тут вы должны писать название вашего продукта')
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='product_images')
    descriptions = models.TextField()
    count = models.IntegerField(default=0)
    link = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# Модель для корзины
# Копировать этот модель и изменить модель на WishlistModel
class CartModel(models.Model):
    user_id = models.IntegerField()  # 3
    user_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)  # Product
    user_product_quantity = models.IntegerField(default=0)  # 10
    user_add_date = models.DateTimeField(auto_now_add=True)  # 20:20,12july2024

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

class CartModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'total_price', 'total_count', 'created_at')
    search_fields = ('product',)
    list_filter = ('created_at',)

admin.site.register(CartModel, CartModelAdmin)
