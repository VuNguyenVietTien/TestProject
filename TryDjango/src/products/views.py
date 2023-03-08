from django.shortcuts import render
from .models import Product, ProductImage
from django.shortcuts import redirect
from .forms import ProductForm, ProductImageForm
import json


# Create your views here.
def home(request, *args, **kwargs):
    return render(request, "home.html",{})

def login(request, *args, **kwargs):
    return render(request, "login.html",{})

def about(request, *args, **kwargs):
    return render(request, "about.html",{})

def contact(request, *args, **kwargs):
    return render(request, "contact.html",{})

def create_product(request):
    if request.method == "POST":
        productForm = ProductForm(request.POST)
        productImageForm = ProductImageForm(request.POST, request.FILES)
        if productForm.is_valid() and productImageForm.is_valid():
            product = productForm.save()
            for image in request.FILES.getlist('image'):
                ProductImage.objects.create(image=image, product=product)
            return redirect('/products/list')
    else:
        productForm = ProductForm()
        productImageForm = ProductImageForm()
    return render(request, "create_product.html",{'productForm':productForm, 'productImageForm':productImageForm})

def list_product(request):
    products = Product.objects.all()
    print("this is list product: ",products)
    context = {
        'product_list':products
    }
    return render(request, "list_product.html", context)

def edit_product(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(id=product_id)
        productForm = ProductForm(instance=product)
        productImageForm = ProductImageForm()
        images = ProductImage.objects.filter(product=product)
        images = [image.image.url for image in images]
        context = {
            'productForm':productForm,
            'productImageForm':productImageForm,
            'images': images
        }
        return render(request, "edit_product.html", context)
    else:
        product = Product.objects.get(id=product_id)
        productImage = product.productimage_set.all()
        productImage.delete()

        productForm = ProductForm(request.POST, instance=product)
        productImageForm = ProductImageForm(request.POST or None, request.FILES)
        if productForm.is_valid():
            productForm.save()
            print('productImageForm isvalid = ', productImageForm.is_valid())
            if productImageForm.is_valid():
                for image in request.FILES.getlist('image'):
                    ProductImage.objects.create(image=image, product=product)
    return redirect('products:list_product')

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    productImage = product.productimage_set.all()
    product.delete()
    productImage.delete()
    return redirect('products:list_product')

def detail_product(request, product_id):
    product = Product.objects.get(id=product_id)
    images = product.productimage_set.all()
    images = [image.image.url for image in images]
    context = {
        "product": product,
        'images': images
    }
    return render(request, "detail_product.html", context)

# list all product view