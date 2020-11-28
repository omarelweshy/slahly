from django.contrib import admin
from django.urls import path, include
import pages

admin.site.site_header = 'ادارة صلحلى'
admin.site.index_title = 'صلحلى'
admin.site.site_title = ' صلحلى'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('', include('users.urls')),
]
