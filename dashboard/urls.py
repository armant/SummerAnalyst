from django.conf.urls import patterns, include, url

import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SummerAnalyst.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'edit-firm-name/$', views.edit_firm_name, name='edit_firm_name'),
    url(r'edit-contact-name/$', views.edit_contact_name,
            name='edit_contact_name'),
    url(r'edit-contact-position/$', views.edit_contact_position,
            name='edit_contact_position'),
    url(r'edit-firm-status/$', views.edit_firm_status,
            name='edit_firm_status'),
)