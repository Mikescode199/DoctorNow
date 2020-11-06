from django.views.generic import ListView, TemplateView
import requests


class Menu(TemplateView):
    template_name = 'examples/dashboard.html'
    
    def get(self, request, *args, **kwargs):
        self.object = None
        url = requests.get('https://api.imgflip.com/get_memes')
        response = requests.get(url)
        obj = response.json()

        return self.render_to_response(
               self.get_context_data(
               name = obj["id"]
            ))

