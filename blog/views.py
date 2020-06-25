from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Blog


class AllBlogs(ListView):
    model = Blog
    template_name = 'blog/allblogs.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    pk_url_kwarg = 'blog_id'
