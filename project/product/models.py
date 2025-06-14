#imports
from django.db import models
from project.core.models import Can_Be_Monitored
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Product(Can_Be_Monitored):
    name = models.CharField(
        verbose_name = _("Nome do produto"),
        max_length= 100,
        unique=True
    )
    
    slug = models.SlugField(
        _("Slug do produto"),
        unique=True,
        null=False,
        blank=False
    )
    
    price = models.DecimalField(
        verbose_name = _("Preço do produto"),
        max_digits=10,
        decimal_places=2
    )
    
    image = models.ImageField(
        verbose_name=_("Imagem do produto"),
        upload_to='product/image',
        blank=True
    )
    
    description = models.TextField(
        verbose_name=_("Descrição do produto"),
        blank=True
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Produto")
        verbose_name_plural = _("Produtos")
    