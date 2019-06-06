from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.moderator_login, name='login'),
    url(r'^logout/$', views.moderator_logout, name='logout'),
    url(r'^fill_in_the_blanks/$', views.fill_in_the_blanks, name='fill_in_the_blanks'),
    url(r'^ans_the_foll/$', views.ans_the_foll, name='ans_the_foll'),
    url(r'^give_reasons/$', views.give_reasons, name='give_reasons'),
    url(r'^sample_ppr/$', views.sample_ppr, name='sample_ppr'),
    url(r'^f(?P<pk>[0-9]+)/$', views.FillInTheBlanksDetailView.as_view(), name='fill_in_the_blanks_detail'),
    url(r'^a(?P<pk>[0-9]+)/$', views.AnswerTheFollDetailView.as_view(), name='ans_the_foll__detail'),
    url(r'^g(?P<pk>[0-9]+)/$', views.GiveReasonDetailView.as_view(), name='give_reason_detail'),
]
