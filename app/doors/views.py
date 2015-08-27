from utils import JsonMenuView, MenuItem
from .models import Door

class MainMenu(JsonMenuView):
    title = 'Deuren'

    def getMenu(self):
        return [
            MenuItem(door.name,
                     icon='key',
                     statuses=[['on', 'off'][int(door.status)]],
                     action='/blaat'
             ) for door in Door.objects.all()
        ]
