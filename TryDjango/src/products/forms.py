from django import forms
from .models import Product, ProductImage
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class ProductForm(forms.ModelForm):
    product_name = forms.CharField(
        label = "Tên sản phẩm",
        help_text="Vui lòng nhập tên sản phẩm",
        required=True, 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tên sản phẩm'  
                }
            ))
    description = RichTextUploadingField(config_name='default')
    # description = forms.CharField(
    #     label="Mô tả sản phẩm",
    #     help_text="Mô tả cho sản phẩm",
    #     required=False,
    #     widget=CKEditorUploadingWidget(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Nhập mô tả sản phẩm'
    #         }
    #     )
    # )
    price = forms.FloatField(
        label='Giá',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nhập giá sản phẩm',
                'value':0,
                'min':0,
                'step':0.1,
                'oninput':'validity.valid||(value='');',
            }
        )
        )
    image = forms.ModelMultipleChoiceField(
        queryset=ProductImage.objects.none(),
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'form-control',
                }
            )
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance.pk:
    #         self.fields['image'].queryset = self.instance.image.all()

    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'image']
        exclude = ['created_at', 'updated_at']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 200, 'cols': 10}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'product_name': 'Tên sản phẩm',
            'description': 'Mô tả',
            'price': 'Giá',
        }
        help_texts = {
            'product_name': 'Vui lòng nhập tên sản phẩm',
            'description': 'Vui lòng nhập mô tả'
            }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return price

    def clean_name(self):
        name = self.cleaned_data['product_name']
        if not name.isalpha():
            raise forms.ValidationError('Name must be character')
        return name

    # def save(self):
    #     name = self.cleaned_data['product_name']
    #     description = self.cleaned_data['description']
    #     price = self.cleaned_data['price']
    #     return Product.objects.create(product_name=name, description=description, price=price)


class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Ảnh",
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'file', 
                'multiple': True,
                'name':'images',
            }
        )
    )

    class Meta:
        model = ProductImage
        fields = ['image',]
        exclude = ['created_at', 'updated_at']

    def save(self, product):
        image = self.cleaned_data['image']
        return ProductImage.objects.create(image=image, product = product)

ProductFormSet = forms.inlineformset_factory(
    Product, ProductImage, form=ProductImageForm, extra=3, can_delete=True
)

