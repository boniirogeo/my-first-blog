from django.conf.urls import url
from gobanapp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^jobs/(?P<id>[0-9]+)/$', views.job_detail, name='job_detail'),
    url(r'^my_jobs/$', views.my_jobs, name='my_jobs'),
    url(r'^create_job/$', views.create_job, name='create_job'),
    url(r'^edit_job/(?P<id>[0-9]+)/$', views.edit_job, name='edit_job'),
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^checkout/$', views.create_purchase, name='create_purchase'),
    url(r'^penjualan/$', views.penjualan, name='penjualan'),
    url(r'^pembelian/$', views.pembelian, name='pembelian'),
    url(r'^category/(?P<link>[\w|-]+)/$', views.category, name='category'),
    url(r'^search/$', views.search, name='search'),
]
