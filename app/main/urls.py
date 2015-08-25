from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^menu.json$', views.MainMenu.as_view(), name='main_menu'),
    url(r'^status.json$', views.StatusView.as_view(), name='status'),
]
