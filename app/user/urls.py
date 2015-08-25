from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile.json$', views.UserProfile.as_view(), name='profile'),
]
