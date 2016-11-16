from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^list/$', IllustrationList.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', IllustrationView.as_view(), name="detail"),
    url(r'^add/$', IllustrationCreate.as_view(), name="add"),
    url(r'^edit/(?P<pk>\d+)/$', IllustrationEdit.as_view(), name="edit"),
]
