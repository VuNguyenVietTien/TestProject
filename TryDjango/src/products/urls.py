"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from products import views

app_name = "products"
urlpatterns = [
    path('list',views.list_product, name='list_product'),
    path('create',views.create_product, name='create_product'),
    path('edit/<int:product_id>',views.edit_product, name='edit_product'),
    path('delete/<int:product_id>',views.delete_product, name='delete_product'),
    path('detail/<int:product_id>',views.detail_product, name='product_detail'),
]