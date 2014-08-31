from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    # Firm/group line 1: name, application status, deadline, reminder
    # date
    url(r'edit-firm-name/$', views.edit_firm_name, name='edit_firm_name'),
    url(r'edit-firm-status/$', views.edit_firm_status, 
            name='edit_firm_status'),
    url(r'edit-firm-deadline/$', views.edit_firm_deadline, 
            name='edit_firm_deadline'),
    url(r'edit-firm-remind-date/$', views.edit_firm_remind_date, 
            name='edit_firm_remind_date'),

    # Firm/group - line 2: set default reminder time for the contacts in
    # this firm/group
    url(r'edit-firm-recurring-number/$', views.edit_firm_recurring_number,
            name='edit_firm_recurring_number'),
    url(r'edit-firm-recurring-type/$', views.edit_firm_recurring_type,
            name='edit_firm_recurring_type'),

    # Contact info: name, position, the date of the last contact,
    # reminder settings
    url(r'edit-contact-name/$', views.edit_contact_name,
            name='edit_contact_name'),
    url(r'edit-contact-position/$', views.edit_contact_position,
            name='edit_contact_position'),
    url(r'edit-contact-last-contact/$', views.edit_contact_last_contact, 
            name='edit_contact_last_contact'),
    url(r'edit-contact-recurring-number/$', 
            views.edit_contact_recurring_number,
            name='edit_contact_recurring_number'),
    url(r'edit-contact-recurring-type/$', views.edit_contact_recurring_type,
            name='edit_contact_recurring_type'),
    url(r'edit-contact-remind-date/$', views.edit_contact_remind_date, 
            name='edit_contact_remind_date'),
    
    # Periodic contact reminder and specific date contact reminder:
    # nullify one when the other one is clicked on.
    url(r'nullify-contact-remind-date/$', views.nullify_contact_remind_date, 
            name='nullify_contact_remind_date'),
    url(r'nullify-contact-remind-periodic/$',
            views.nullify_contact_remind_periodic,
            name='nullify_contact_remind_periodic'),

    # New firm
    url(r'^new-firm/$', login_required(views.NewFirmView.as_view(), login_url='/login/'), name='NewFirmView'),
)