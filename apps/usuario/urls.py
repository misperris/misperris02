from django.conf.urls import url
from apps.usuario.views import RegistroUsuario

app_name = 'i_usuario'

urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name="registrar")
    

]