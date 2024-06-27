#Импортируется модуль admin из пакета django.contrib.
#Импортируется модель MyModel из локального модуля models.
from django.contrib import admin
from .models import CategoryModel, ProductModel, CartModel

# Создаём класс MyModelAdmin:
# Создаем админ панель для категории

#list_display: Определяет поля, которые будут отображаться в списке объектов в админке.
#search_fields: Определяет поля, по которым можно выполнять поиск.
#list_filter: Определяет поля, по которым можно фильтровать список объектов.
@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title']
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at']

# Регистрируем модель MyModel с настройками, определёнными в классе MyModelAdmin.
@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title', 'price']
    list_display = ['id', 'title', 'price', 'count', 'updated_at', 'created_at']
    list_filter = ['created_at']

admin.site.register(CartModel)

