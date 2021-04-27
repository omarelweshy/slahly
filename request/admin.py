from django.contrib import admin
from .models import Request

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ["__str__", "status", "get_user_name", "employee"]
    list_filter = ("status", "employee")
    search_fields = ('problem', 'id',)

    def get_user_name(self, obj):
        return obj.user.full_name

    get_user_name.short_description = 'العميل'
