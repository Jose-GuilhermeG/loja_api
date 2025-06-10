#imports
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

#models
from .models import Product

#model admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ['name']
    search_help_text = _("Pesquisar produto pelo nome")
    

# Register your models here.
admin.site.register(Product,ProductAdmin)