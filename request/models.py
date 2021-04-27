from django.db import models
from django.utils.translation import gettext as _
from service.models import Employee
from django.contrib.auth import get_user_model

class Request(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, verbose_name=_("الموظف"), on_delete=models.SET_NULL, null=True)
    problem = models.TextField(_("المشكلة"))
    date = models.DateTimeField(_("وقت الطلب"), auto_now=True)
    status = models.BooleanField(_("تم تنفيذ الخدمة"), default=False)
    show_in_history = models.BooleanField(_("إظهار فى السجل"), default=True)

    def __str__(self):
        return 'الطلب # %s للموظف %s' % (self.id, self.employee)

    class Meta:
        verbose_name = _('الطلب')
        verbose_name_plural = _('الطلبات')
        ordering = ['-id']