from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landpage.urls')),
]

handler404 = 'error.views.handler404'

handler500 = 'error.views.handler500'

handler403 = 'error.views.handler403'