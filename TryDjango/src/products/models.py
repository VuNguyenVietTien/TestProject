from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=120)
    description  = RichTextUploadingField(default=None)
    price        = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    active       = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.SET_DEFAULT, default=1)
    
    
    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.pk})

    def get_detail_url(self):
        return reverse("products:product_detail", kwargs={"product_id":self.id})

    def get_edit_url(self):
        return reverse("products:edit_product", kwargs={"product_id":self.id})

class ProductImage(models.Model):
    image        = models.ImageField(upload_to='images/', blank=True, null=True)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active    = models.BooleanField(default=True)
    is_main      = models.BooleanField(default=False)
    created      = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated      = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.product_name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

class User(models.Model):
    first_name      = models.CharField(max_length=120)
    last_name       = models.CharField(max_length=120)
    username        = models.CharField(max_length=120)
    password        = models.CharField(max_length=50,blank=True, null=True)
    email           = models.EmailField(null=False)
    phone_number    = models.IntegerField(null=True)
    birthday        = models.DateField(null=True)
    address         = models.TextField(null=True)
    avatar          = models.ImageField(null=True)
    role            = models.IntegerField(default=1)


class Category(models.Model):
    name            = models.CharField(max_length=120)
    description     = models.TextField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name            = models.CharField(max_length=120)
    description     = models.TextField(null=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price     = models.IntegerField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    status          = models.IntegerField(default=1)
    address         = models.TextField(null=True)
    phone_number    = models.IntegerField(null=True)
    note            = models.TextField(null=True)

class Comment(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    content         = models.TextField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    status          = models.IntegerField(default=1)

class Rating(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate            = models.IntegerField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity        = models.IntegerField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    status          = models.IntegerField(default=1)

class OrderDetail(models.Model):
    order           = models.ForeignKey(Order, on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity        = models.IntegerField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    status          = models.IntegerField(default=1)
    price           = models.IntegerField(null=True)

class OrderStatus(models.Model):
    name            = models.CharField(max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)