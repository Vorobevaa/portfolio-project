from django.shortcuts import get_object_or_404
from .models import Blog
from django.views.generic.list import ListView
from django.views.generic import DetailView


class Allblogs(ListView):
    model = Blog
    template_name = 'blog/allblogs.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    pk_url_kwarg = 'blog_id'
