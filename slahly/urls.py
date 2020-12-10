from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import pages

admin.site.site_header = 'ادارة صلحلى'
admin.site.index_title = 'صلحلى'
admin.site.site_title = ' صلحلى'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('', include('users.urls')),
    path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns