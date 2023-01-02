from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('' , views.emBreve, name = 'index'),
   path('sucesso' , views.success, name = 'sucesso'),
   path('falha' , views.falha, name = 'falha'),
   path('aviso-de-privacidade', views.privacidade),
   path('trabalhe', views.land),
   path('creditos', views.creditos),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
