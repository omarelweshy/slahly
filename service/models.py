from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from djmoney.models.fields import MoneyField


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("اسم الخدمة"), max_length=50)
    image = models.ImageField(_("صورة الخدمة"), upload_to='service_images')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employees', args=[str(self.id)])
        
    class Meta:
            verbose_name = _('الخدمة')
            verbose_name_plural = _('الخدمات')


class Employee(models.Model):
    service = models.ForeignKey(Service, verbose_name=_("الخدمة"), on_delete=models.CASCADE, related_name='employee')
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("اسم الموظف"), max_length=50)
    photo = models.ImageField(_("صورة الموظف"))
    about = models.CharField(_("معلومات الموظف"), max_length=225)


    def __str__(self):
        return self.name

    class Meta:
            verbose_name = _('الموظف')
            verbose_name_plural = _('الموظفين')

class SpareParts(models.Model):
    service = models.ForeignKey(Service, verbose_name=_("الخدمة"), on_delete=models.CASCADE, related_name='spare_part')
    name = models.CharField(_("اسم القطعة"), max_length=225)
    price = MoneyField(_("اسم القطعة"), max_digits=14, decimal_places=2, default_currency='EGP')
    details = models.CharField(_("التفاصيل"), max_length=225)
    photo = models.ImageField(_("صورة المنتج"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('قطعة الغيار')
        verbose_name_plural = _('قطع الغيار')