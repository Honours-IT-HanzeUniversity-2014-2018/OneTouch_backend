from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from utils import JsonMenuView, JsonItemView, MenuItem
from .models import Door

class DoorMenuItem(MenuItem):
    def __init__(self, door):
        super(DoorMenuItem, self).__init__(
            door.name,
            icon='key',
            statuses=[['status-on', 'status-off'][int(door.status)]],
            action=reverse('doors:toggle_door', kwargs={'pk': door.pk})
        )

class MainMenu(JsonMenuView):
    title = 'Deuren'

    def getMenu(self):
        return [DoorMenuItem(door) for door in Door.objects.all()]

class ToggleDoor(JsonItemView):
    def getMenu(self):
        door = get_object_or_404(Door, pk=self.kwargs['pk'])
        door.toggle()

        return DoorMenuItem(door)
