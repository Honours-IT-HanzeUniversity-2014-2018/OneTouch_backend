from django.core.urlresolvers import reverse
from utils import JsonMenuView, MenuItem


class MainMenu(JsonMenuView):
    def getMenu(self):
        return [
            MenuItem('Zender', icon="zap"),
            MenuItem('Aanzetten', icon="on-off", statuses=['red-icon']),
            MenuItem('Volume', icon="volume"),
        ]
