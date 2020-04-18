from .models import Job
from django.views.generic.list import ListView


class Home(ListView):
    model = Job
    template_name = 'jobs/home.html'
