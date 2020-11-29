from django.db import models
from stdimage import StdImageField
from django.utils.translation import gettext as _

class Service(models.Model):
    name = models.CharField(_("اسم الخدمة"), max_length=50)
    image = models.ImageField(_("صورة الخدمة"), upload_to='service_images')

    def __str__(self):
        return self.name
    
    class Meta:
            verbose_name = _('الخدمة')
            verbose_name_plural = _('الخدمات')