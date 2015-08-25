from django.conf.urls import *

urlpatterns = patterns('',
                       (r'^api/v1/user/', include('user.urls', namespace='user')),
                       (r'^api/v1/television/', include('television.urls', namespace='television')),
                       (r'^api/v1/main/', include('main.urls', namespace='main'))
                       )
