from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gestao import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial, name='pagina_inicial')
]

# Essa linha abaixo é o "disjuntor" que libera as fotos no navegador
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)