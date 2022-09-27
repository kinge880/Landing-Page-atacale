from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('' , views.land, name = 'index'),
   path('/enviando...' , views.land, name = 'load_submit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
