from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog_list'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='catalog_detail'),
    path('catalog/create', ProductCreateView.as_view(), name='catalog_create'),
    path('catalog/<int:pk>/update', ProductUpdateView.as_view(), name='catalog_update'),
    path('catalog/<int:pk>/delete', ProductDeleteView.as_view(), name='catalog_delete'),
    path('users/', include('users.urls')),


]
