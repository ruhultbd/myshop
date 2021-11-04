from django.urls import path
from .views import Products, TaggedProducts, AddView, CategoryListView, CategoryEditView, CategoryDeleteView

from . import views

urlpatterns = [
    path('', Products.as_view(), name="products"),
    path('tag/<str:tag>', TaggedProducts.as_view(), name="products.tag"),
    path('create', AddView.as_view(), name="product.add"),

    path('categories', CategoryListView.as_view(), name="product-categories"),
    path('category/edit/<int:id>', CategoryEditView.as_view(), name="category.edit"),
    path('category/delete/<int:id>', CategoryDeleteView.as_view(), name="category.delete"),

]
