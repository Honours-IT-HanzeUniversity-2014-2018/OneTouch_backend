from .models import Door


def process_speech(command):
    # This one is kind of simple. We only 'toggle' the doors status, so it can either open or close, but the
    # behaviour is actually determined by reading from the database. Therefor, it does not really matter all that much
    # what the user said. We may assume they want to open or close a door, as long as the command includes a name of one
    # of the doors in the database. As the status of these doors is being saved in the database, we can simply call the
    # toggle() definition on the database entry object.

    words = command.split(' ')
    matches = Door.objects.filter(name__in=words)

    for match in matches:
        match.toggle()

    return len(matches) > 0
