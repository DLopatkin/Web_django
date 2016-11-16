from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic import CreateView
from .views import *


app_name = 'main'
urlpatterns = [
    url(r'^$', main_page, name='main_page'),
    url(r'^users/(?P<pk>\d+)/$', UserView.as_view(), name="user"),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^register/', CreateView.as_view(template_name='registration/registration.html',
                                          form_class=MyUserForm,
                                          success_url='/',),
                                          name="register"),
    url(r'^user_edit/(?P<pk>\d+)/$', UserEdit.as_view(), name="edit"),
]
