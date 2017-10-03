from django.conf.urls import url

from . import views

app_name = 'tickets'

urlpatterns = [
    url(r'^$', views.ListRequestView.as_view(), name='requests_list'),
    url(r'^new$', views.request_new, name='request_new'),
    url(r'^(?P<pk>[0-9]+)/$', views.request_detail, name='request_detail'),
    url(r'^request/(?P<pk>[0-9]+)/edit/$', views.request_edit, name='request_edit'),
]
