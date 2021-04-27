from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

admin.site.site_header = 'ادارة صلحلى'
admin.site.index_title = 'صلحلى'
admin.site.site_title = ' صلحلى'

class HomeView(TemplateView):
    template_name = "home.html"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('service/', include('service.urls')),
    path('employee/', include('employee.urls')),
    path('requests/', include('request.urls')),
    path('contact/', include('contact.urls')),
    path('', include('store.urls')),
    path('', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
