from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

GENDER_CHOICES = [('MALE', 'أنثى'), ('FEMALE', 'ذكر')]


class User(AbstractUser):
    first_name = models.CharField(_("الاسم الاول"), max_length=20)
    last_name = models.CharField(_("الاسم الاخير"), max_length=20)
    address = models.CharField(
        _("العنوان التفصيلى"), max_length=225, blank=False, editable=True)
    phone = models.IntegerField(_("رقم الهاتف"), unique=True, null=True)
    email = models.EmailField(_("البريد الالكترونى"), max_length=254, unique=True)

    class Meta:
        verbose_name = _('المستخدم')
        verbose_name_plural = _('المستخدمين')

    @property
    def full_name(self):
        """Returns the person's full name."""
        return '%s %s' % (self.first_name, self.last_name)