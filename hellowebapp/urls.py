from collection.backends import MyRegistrationView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import(
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)

urlpatterns = patterns('',
    url(r'^$', 'collection.views.index', name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
        
    url(r'^services/$',
        RedirectView.as_view(pattern_name='browse')),
    url(r'^services/(?P<slug>[-\w]+)/$',
        'collection.views.service_detail',
        name='service_detail'),
    url(r'^services/(?P<slug>[-\w]+)/edit/$',
        'collection.views.edit_service', name='edit_service'),
    
    #browse URLs
    url(r'^browse/$', RedirectView.as_view(
        pattern_name='browse')),
    url(r'^browse/name/$', 'collection.views.browse_by_name', name='browse'),
    url(r'^browse/name/(?P<initial>[-\w]+)/$', 'collection.views.browse_by_name',
        name='browse_by_name'),
    
    #password reset URLs
    url(r'^accounts/password/reset/$', password_reset,
        {'template_name': 'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name="password_reset_done"), 
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$',
        password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),
        
    #register URLs
    url(r'^accounts/register/$', MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/create_service/$',
        'collection.views.create_service',
        name='registration_create_service'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
)