
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include

from informatii.views import informatii_view, get_details


urlpatterns = [
    path('', informatii_view, name='informatii'),
    path('detalii/', get_details, name='detalii'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)