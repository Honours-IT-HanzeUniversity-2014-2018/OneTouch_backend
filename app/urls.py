from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^api/v1/user/', include('user.urls', namespace='user')),
                       (r'^api/v1/television/', include('television.urls', namespace='television')),
                       (r'^api/v1/doors/', include('doors.urls', namespace='doors')),
                       (r'^api/v1/main/', include('main.urls', namespace='main')),

                       (r'^admin/', include(admin.site.urls)),
                       )
