from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.conf import settings
from django.urls import reverse

GENDER_CHOICES = [('MALE', 'أنثى'), ('FEMALE', 'ذكر')]


class User(AbstractUser):
    first_name = models.CharField(_("الاسم الاول"), max_length=20)
    last_name = models.CharField(_("الاسم الاخير"), max_length=20)
    location = models.CharField(
        _("Location"), max_length=50, blank=True, editable=True)
    email = models.EmailField(_("البريد الالكترونى"), max_length=254, unique=True)
    photo = models.ImageField(_("الصورة الشخصية"), upload_to="profile_images",
                              max_length=None, default='profile_images/default.jpg', blank=True)
    gender = models.CharField(
        _("الجنس"), max_length=50, choices=GENDER_CHOICES)

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.slug)])

    @property
    def full_name(self):
        """Returns the person's full name."""
        return '%s %s' % (self.first_name, self.last_name)