from django.contrib import admin
from django.urls import path, include
from inscricoes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/', include('inscricoes.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
