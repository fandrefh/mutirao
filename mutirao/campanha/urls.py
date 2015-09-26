from django.conf.urls import url

from mutirao.campanha.views import add_campanha

urlpatterns = [
    url(r'^adicionar/$', add_campanha, name='addcampanha'),
]
