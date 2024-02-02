from . import views
from django.urls import path

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard),
    path('product-list', views.products),
    path('product-create', views.product_create),
    path('product_update/<int:id>', views.product_update,name='product_update'),
    path('product_detail/<int:id>', views.product_detail,name='product_detail'),

]