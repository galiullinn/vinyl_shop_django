from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from products.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)