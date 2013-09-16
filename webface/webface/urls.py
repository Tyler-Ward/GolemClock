from django.conf.urls import patterns, include, url
import golem.views as golem

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webface.views.home', name='home'),
    # url(r'^webface/', include('webface.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', golem.index_view),
    url(r'^login$', golem.login_view),
    url(r'^logout$', golem.logout_view),
    url(r'^main$', golem.main_view),
    url(r'^snooze-alarm$', golem.snooze_alarm_view),
    url(r'^stop-alarm$', golem.stop_alarm_view),
    
    url(r'^test/display', golem.test_display_view),
)
