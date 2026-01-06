from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

    urlpatterns += [
        re_path(r'^(?P<path>css/.*)$', serve, {'document_root': settings.STATICFILES_DIRS[0]}),
        re_path(r'^(?P<path>img/.*)$', serve, {'document_root': settings.STATICFILES_DIRS[0]}),
        re_path(r'^(?P<path>js/.*)$', serve, {'document_root': settings.STATICFILES_DIRS[0]}),
        re_path(r'^(?P<path>lib/.*)$', serve, {'document_root': settings.STATICFILES_DIRS[0]}),
    ]
