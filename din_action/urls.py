from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^select_action$', views.select_action, name='select_action'),
    url(r'^$', views.din_action, name='din_action'),
]