from django.contrib import admin
from .models import *
from django.utils.translation import gettext as _



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

