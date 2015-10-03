from django.conf.urls import url

from mutirao.campanha import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^adicionar/$', views.add_campanha, name='add_campanha'),
]
