import json
from django.http import HttpResponse
from django.views.generic import View


class UserProfile(View):
    def get(self, *args, **kwargs):
        response = {
            'success': True,
            'profile': {
                'fullname': 'Jeroen',
                'picture':  self.request.build_absolute_uri('/static/user_picture.jpg')
            }
        }

        return HttpResponse(json.dumps(response),
                            content_type="application/json")
