from django.conf.urls import url
from gobanapp import views

urlpatterns = [
url(r'^$', views.home, name='home'),
url(r'^jobs/(?P<id>[0-9]+)/$', views.job_detail, name='job_detail'),
]
