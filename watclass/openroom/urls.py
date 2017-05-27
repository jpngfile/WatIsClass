
from django.conf.urls import url

from . import views
from django.conf.urls import url

from . import views
app_name = 'openroom'
# noinspection PyPep8,PyPep8,PyPep8,PyPep8
urlpatterns = [
    url(r'generate/$', views.generate, name='generate'),
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search')
]
