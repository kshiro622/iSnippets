from django.conf.urls import url
from . import views

app_name="snippets"

urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^manage/$', views.manage, name='manage')
]