import json
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View
from utils import JsonMenuView, MenuItem


class MainMenu(JsonMenuView):
    def getMenu(self):
        return [
            MenuItem('Televisie', icon="ios-monitor", action=reverse('television:main_menu')),
            MenuItem('Deuren', icon="ios-home", action=reverse('doors:main_menu')),
        ]


class StatusView(View):
    def get(self, *args, **kwargs):
        response = {'success': True}
        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )
