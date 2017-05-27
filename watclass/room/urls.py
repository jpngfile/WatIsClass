from django.conf.urls import url

from . import views
from django.conf.urls.static import static

app_name = 'room'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[A-z]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[A-z]+)/(?P<lecture_id>[0-9]+)/$', views.lecture, name='lecture'),
    url(r'(?P<question_id>[A-z]+)/$',views.detail, name = 'detail')

]
