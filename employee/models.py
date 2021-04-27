from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth import get_user_model
from service.models import Employee



class EmployeeWOrkImages(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=_("العامل"), on_delete=models.SET_NULL, null=True, related_name='work_image')
    images = models.ImageField(_("صورة العمل"), upload_to='employee_work_images', height_field=None, width_field=None, max_length=None)

    class Meta:
            verbose_name = _('صورة العمل')
            verbose_name_plural = _('صور العمل')

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='comments')
    comment = models.CharField(_("التعليق"), max_length=250)
    created_at = models.DateTimeField(_("وقت التعليق"), auto_now=True)

    def __str__(self):
        return 'التعليقات على الموظف %s' % self.employee

    def get_absolute_url(self):
        return reverse('employee_detail', kwargs={'pk':self.pk})
    class Meta:
            verbose_name = _('التعليق')
            verbose_name_plural = _('التعليقات')