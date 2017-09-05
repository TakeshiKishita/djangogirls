from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls'), name='blog'),
    #url(r'^payroll/', include('payroll.urls'), name = 'payroll'),
    url(r'^blog/accounts/login/$', views.login, name='login'),
    url(r'^blog/accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/blog/'}),
]