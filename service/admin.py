from django.contrib import admin
from .models import *
from django.utils.translation import gettext as _

admin.site.register(Service)
admin.site.register(Employee)
admin.site.register(SpareParts)

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ["__str__", "done", "get_user_name", "employee"]
    list_filter = ("done", "employee")

    def get_user_name(self, obj):
        return obj.user.full_name

    get_user_name.short_description = 'العميل'
