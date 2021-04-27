from django.db import models
from django.utils.translation import gettext as _
from djmoney.models.fields import MoneyField
from service.models import Service
# Create your models here.
class SpareParts(models.Model):
    service = models.ForeignKey(Service, verbose_name=_("الخدمة"), on_delete=models.SET_NULL, null=True, related_name='spare_part')
    name = models.CharField(_("اسم القطعة"), max_length=225)
    price = MoneyField(_("سعر القطعة"), max_digits=14, decimal_places=2, default_currency='EGP')
    details = models.CharField(_("التفاصيل"), max_length=225)
    photo = models.ImageField(_("صورة المنتج"), upload_to='SpareParts_images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('قطعة الغيار')
        verbose_name_plural = _('قطع الغيار')
