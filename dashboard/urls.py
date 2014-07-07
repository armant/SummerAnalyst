from django.conf.urls import patterns, include, url

import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SummerAnalyst.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
)