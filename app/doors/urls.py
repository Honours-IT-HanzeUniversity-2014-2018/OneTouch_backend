from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^menu.json$', views.MainMenu.as_view(), name='main_menu'),
    url(r'^toggle/(?P<pk>[\d]+).json$', views.ToggleDoor.as_view(), name='toggle_door'),
]
