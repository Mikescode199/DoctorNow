from django.views.generic import ListView, TemplateView
import requests
import json

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    
    
class Menu(TemplateView):
    template_name = 'examples/dashboard.html'
    
    def get(self, request, *args, **kwargs):
        self.object = None
        params = { 'order': 'desc' }
        response = generate_request('https://breaking-bad-quotes.herokuapp.com/v1/quotes', params)
        data_string = json.dumps(response)
        decoded = json.loads(data_string)
        return self.render_to_response(
            self.get_context_data(
            noticia = decoded[0]['quote'],
            autor = decoded[0]['author']
            ))

