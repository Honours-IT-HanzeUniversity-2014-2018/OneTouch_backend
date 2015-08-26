from utils import JsonMenuView, MenuItem


class MainMenu(JsonMenuView):
    title = 'Deuren'

    def getMenu(self):
        return [
            MenuItem('Voordeur', icon="key"),
            MenuItem('Achterdeur', icon="key"),
        ]
