from django.contrib import admin
from .models import *
from django.utils.translation import gettext as _

admin.site.register(Service)
admin.site.register(SpareParts)

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ["__str__", "status", "get_user_name", "employee"]
    list_filter = ("status", "employee")

    def get_user_name(self, obj):
        return obj.user.full_name

    get_user_name.short_description = 'العميل'

class WorkImagesInline(admin.TabularInline):
    model = EmployeeWOrkImages

class CommentInline(admin.TabularInline):
    model = Comment

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [
        WorkImagesInline,
        CommentInline,
    ]


admin.site.register(Employee, EmployeeAdmin)

