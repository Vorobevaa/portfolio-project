from django.views.generic.list import ListView

from .models import Job


class Home(ListView):
    model = Job
    template_name = 'jobs/home.html'
