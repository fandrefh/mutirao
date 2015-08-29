from django.conf.urls import url

from mutirao.core.views import home, cadastro_usuario, sucesso_usuario

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^cadastro-usuario/$', cadastro_usuario, name='cadastrousuario'),
    url(r'^sucesso-usuario/$', sucesso_usuario, name='usuariosucesso'),
]
