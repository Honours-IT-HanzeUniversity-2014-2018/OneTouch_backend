from django.core.urlresolvers import reverse
from utils import JsonMenuView, MenuItem


class MainMenu(JsonMenuView):
    def getMenu(self):
        return [
            MenuItem('Aanzetten', icon="power", statuses=['red-icon']),
            MenuItem('Zender', icon="grid"),
            MenuItem('Volume +', icon="volume-high"),
            MenuItem('Volume -', icon="volume-low"),
        ]
