from utils import JsonMenuView, MenuItem


class MainMenu(JsonMenuView):
    def getMenu(self):
        return [
            MenuItem('Voordeur', icon="key"),
            MenuItem('Achterdeur', icon="key"),
        ]
