from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from catalog.models import Product, Version

from catalog.form import ProductForm, VersionForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

def save_feedback_to_file(name, email, message, filename='feedback.txt'):
    with open(filename, 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Message: {message}\n")
        file.write("="*40 + "\n")


class ProductListView(ListView):
    model = Product
    # template_name = 'catalog/product_list.html'
    # сontext_object_name = 'product'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # Получаем все продукты
    #     products = context['product']
    #
    #     # Для каждого продукта выбираем текущую (активную) версию
    #     for product in products:
    #         active_version = product.versions.filter(is_current=True).first()
    #         product.active_version = active_version
    #
    #     return context

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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

# def product_about(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, 'products/product_about.html', context)
#

#CRUD >>>
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_list')



class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_list')

    def get_success_url(self):
        return reverse('catalog:catalog_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_list')

