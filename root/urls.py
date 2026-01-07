from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps import views as app_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', app_views.login_view, name='login'),
    path('register/', app_views.register_view, name='register'),
    path('logout/', app_views.logout_view, name='logout'),
    path('', app_views.index, name='home'),
    path('about/', app_views.about, name='about'),
    path('blog/', app_views.blog, name='blog'),
    path('contact/', app_views.contact, name='contact'),
    path('feature/', app_views.feature, name='feature'),
    path('menu/', app_views.menu, name='menu'),
    path('team/', app_views.team, name='team'),
    path('testimonial/', app_views.testimonial, name='testimonial'),
    path('loxotron/', app_views.loxotron, name='loxotron'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# Custom 404 handler
handler404 = 'apps.views.page_not_found'

# Add explicit /404 path for navbar button
urlpatterns.append(path('404', app_views.page_not_found, name='404'))
