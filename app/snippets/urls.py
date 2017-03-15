from django.conf.urls import url
from . import views

app_name="snippets"

urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^home/$', views.home, {'snippet_id': 1}, name='home'),
    url(r'^delete/(?P<snippet_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^home/(?P<snippet_id>[0-9]+)/$', views.home, name='update')
]