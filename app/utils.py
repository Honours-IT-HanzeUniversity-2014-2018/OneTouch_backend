import json
from django.http import HttpResponse
from django.views.generic import View
import types


class JsonMenuView(View):
    menu = []
    title = "Menu"

    def getMenu(self):
        return self.menu

    def get(self, *args, **kwargs):
        items = [item.__dict__ for item in self.getMenu()]

        response = {
            'success': True,
            'type': 'menu',
            'data': items
        }

        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )


class MenuItem:
    title = None
    icon = None
    action = None
    statuses = None

    def __init__(self, title, icon=None, action=None, statuses=None):
        if statuses is not None and not isinstance(statuses, types.ListType):
            raise TypeError('Statuses must be a list of applicable statuses')

        self.title = title
        self.icon = icon
        self.action = action
        self.statuses = statuses
