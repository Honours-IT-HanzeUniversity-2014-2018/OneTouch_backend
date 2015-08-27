import json
from django.http import HttpResponse
from django.views.generic import View
import types


class JsonMenuView(View):
    menu = []
    title = "Menu"
    show_profile = False

    def getMenu(self):
        return self.menu

    def get(self, *args, **kwargs):
        items = [item.__dict__ for item in self.getMenu()]

        response = {
            'success': True,
            'type': 'menu',
            'data': items,
            'title': self.title,
            'show_profile': self.show_profile
        }

        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )


class JsonItemView(View):
    menu = None
    
    def getMenu(self):
        return self.menu

    def get(self, request, *args, **kwargs):
        response = {
            'success': True,
            'data': self.getMenu().__dict__,
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
    is_menu = False

    def __init__(self, title, icon=None, action=None, statuses=None, is_menu=False):
        if statuses is not None and not isinstance(statuses, types.ListType):
            raise TypeError('Statuses must be a list of applicable statuses')

        self.title = title
        self.icon = icon
        self.action = action
        self.statuses = statuses
        self.is_menu = is_menu

