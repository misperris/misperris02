
from django.conf.urls import url, include
from apps.mascota.views import index

app_name = 'i_mascota'
urlpatterns = [
    url(r'^$', index),
]