from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^bookmark/(?P<pk>\d+)$', BookmarkView.as_view(), name="add"),
]
