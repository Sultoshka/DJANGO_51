from django.shortcuts import render, redirect
from django.views.generic import ListView
from products.handler import bot
from django.contrib import messages

from .forms import SearchForm
from .models import CategoryModel, ProductModel, CartModel
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Cart, CartItem

def delete_product_from_cart(request, cart_id, product_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    messages.success(request, 'Product removed from cart.')
    return redirect('cart_detail', cart_id=cart_id)

# def home_page(request):
#
#     categories = CategoryModel.objects.all()
#     products = ProductModel.objects.all()
#     # print -> Laptops,smart,pencil
#     context = {'categories': categories, 'products': products}
#     return render(request, template_name='index.html', context=context)

class HomePage(ListView):
    template_name = 'index.html'
    model = ProductModel
    context_object_name = 'products'
    form_class = SearchForm
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        return context


def search(request):
    # search=='Iphone12'
    if request.method == 'POST':
        # <input name='search_product'> <button>
        get_product = request.POST.get('search_product')
        # search_product=Iphone12 Iphone13
        try:
            exact_product = ProductModel.objects.get(title__icontains=get_product)
            return redirect(f'/products/{exact_product.id}')
        except:
            return redirect('/')


# Iphone12 -> Iphone12,price,
def product_page(request, id):
    product = ProductModel.objects.get(id=id)
    context = {'product': product}
    return render(request, template_name='single-product.html',
                  context=context)


# Функция для добавлении в корзину 3
# Копировать эту функицю и изменить его на add_product_to_wishlist
def add_product_to_cart(request, id):
    if request.method == 'POST':
        checker = ProductModel.objects.get(id=id) #2
        if checker.count >= int(request.POST.get('pr_count')):
            CartModel.objects.create(user_id=request.user.id,
                                     user_product=checker,
                                     user_product_quantity=int(request.POST.get('pr_count')))
            print('Success')
            return redirect('/user_cart')
        else:
            print('Error')
            messages.info(request, 'Вы превысили кол-во товара!')
            return redirect('/')


# Копировать эту функцию сделать user_wishlist
def user_cart(request):
    # Если в таблице Корзина есть пользователь с определенным id
    cart = CartModel.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        main_text = 'Новый заказ ока!'

        for i in cart:
            main_text += f'\n Товар: {i.user_product}\n' \
                         f'Кол-во: {i.user_product_quantity}\n' \
                         f'ID пользователя: {i.user_id}\n' \
                         f'Цена: {i.user_product.price}\n'
            bot.send_message(-1002161971742, main_text)
            cart.delete()
            return redirect('/')
    else:
        return render(request, template_name='cart.html', context={'cart': cart})
