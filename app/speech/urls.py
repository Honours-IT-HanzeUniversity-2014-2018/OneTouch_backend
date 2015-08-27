from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^process.json$', views.Processor.as_view(), name='main_menu'),
]