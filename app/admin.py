from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.html import mark_safe
from .models import *
from django import forms

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
