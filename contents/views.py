from django.views.generic.list import ListView

from .models import Content


class Home(ListView):
    model = Content
    template_name = 'contents/home.html'
