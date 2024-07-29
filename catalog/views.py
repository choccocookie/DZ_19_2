from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product
from django.views.generic import ListView, DetailView

def save_feedback_to_file(name, email, message, filename='feedback.txt'):
    with open(filename, 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Message: {message}\n")
        file.write("="*40 + "\n")


class ProductListView(ListView):
    model = Product
    # template_name = 'products/product_list.html'
    # context_object_name = 'products'


# def home(request):
#     latest_products = Product.objects.all().order_by('-created_at')[:5]
#
#     # Вывести последние пять товаров в консоль
#     for product in latest_products:
#         print(f'{product.name}: {product.description}')
#
#     # Вывести список товаров на страницу
#     products = Product.objects.all()
#     context = {"products": products, 'latest_products': latest_products}
#
#     return render(request, 'home.html', context)
#     #return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        save_feedback_to_file(name, phone, message)

        # Обрабатываем данные (например, сохраняем их в базе данных, отправляем email и т.д.)
        # Здесь можно добавить код для обработки данных, например:
        # save_feedback_to_database(name, email, message)


        # Возвращаем ответ пользователю
        return HttpResponse("Спасибо, дорогой, за обратную связь!")

    # Если запрос GET, просто отображаем форму
    return render(request, 'products/contacts.html')

class ProductDetailView(DetailView):
    model = Product

# def product_about(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, 'products/product_about.html', context)
#


