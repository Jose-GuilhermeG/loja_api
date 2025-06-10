#imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Can_Be_Monitored(models.Model):
    created_at = models.DateTimeField(
        verbose_name = _("Criado em"),
        auto_now=True
    )
    
    updated_at = models.DateTimeField(
        verbose_name=_("Atualizado em"),
        auto_now_add=True
    )
    
    class Meta:
        ordering = ['-created_at']
        abstrac = True