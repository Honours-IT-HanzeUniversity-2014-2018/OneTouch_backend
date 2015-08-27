from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from utils import JsonMenuView, JsonItemView, MenuItem
from .models import Door

class MainMenu(JsonMenuView):
    title = 'Deuren'

    def getMenu(self):
        return [
            MenuItem(door.name,
                     icon='key',
                     statuses=[['on', 'off'][int(door.status)]],
                     action=reverse('doors:toggle_door', kwargs={'pk': door.pk})
             ) for door in Door.objects.all()
        ]

class ToggleDoor(JsonItemView):
    def getMenu(self):
        door = get_object_or_404(Door, pk=self.kwargs['pk'])
        door.toggle()

        return MenuItem(door.name,
                        icon='key',
                        statuses=[['on', 'off'][int(door.status)]],
                        action=reverse('doors:toggle_door', kwargs={'pk': door.pk}))
