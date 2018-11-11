
from django.conf.urls import url
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate

app_name= 'i_adopcion'
urlpatterns = [
  url(r'^index$', index_adopcion),
  url(r'^solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar'),
  url(r'^solicitud/$', SolicitudCreate.as_view(), name='solicitud_crear'),  
]