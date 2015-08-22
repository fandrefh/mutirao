from django.conf.urls import url

from mutirao.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]
