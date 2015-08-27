import json, importlib

from django.http import HttpResponse
from django.views.generic import View
from settings import SPEECH_ENABLED_APPS


class Processor(View):
    def get(self, *args, **kwargs):
        return self.http_process_speech(self.request.GET.get('command', ''))

    def post(self, *args, **kwargs):
        return self.http_process_speech(self.request.POST.get('command', ''))

    def http_process_speech(self, command):
        success, handler = False, None

        if command is not '':
            success, handler = self.process_speech(command)

        return HttpResponse(json.dumps({
            'success': success,
            'handler': handler
        }), content_type='application/json')

    def process_speech(self, command):
        for app in SPEECH_ENABLED_APPS:
            handler = importlib.import_module('{0}.speech'.format(app))
            result = handler.process_speech(command)

            if result:
                return True, app

        return False, None
