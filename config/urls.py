from django.contrib import admin
from django.urls import path
from properties.views import apartment_list, apartment_detail, about, contact, calendar_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', apartment_list, name='apartment_list'),
    path('apartment/<int:id>/', apartment_detail, name='apartment_detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('calendar/', calendar_view, name='calendar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)