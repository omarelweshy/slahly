from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

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

CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )


class Employee(models.Model):
    service = models.ForeignKey(Service, verbose_name=_("الخدمة"), on_delete=models.SET_NULL, null=True, related_name='employee')
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("اسم الموظف"), max_length=50)
    photo = models.ImageField(_("صورة الموظف"), upload_to='employee_images')
    rate = models.CharField(_("تقييم الموظف من 5"), choices=CHOICES, max_length=2)
    about = models.CharField(_("معلومات الموظف"), max_length=225)

    def __str__(self):
        return self.name

    class Meta:
            verbose_name = _('الموظف')
            verbose_name_plural = _('الموظفين')


