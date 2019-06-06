from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexx,  name='indexx'),
    url(r'^login/$', views.student_login, name='login'),
    url(r'^result/$', views.result, name='result'),
 ]