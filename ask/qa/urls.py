from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.test, name='test'),
    # url(r'^login/$', views.test, name='test'),
    url(r'^.*$', views.test, name='test'),
]