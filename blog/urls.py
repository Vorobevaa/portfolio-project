from django.urls import path

from blog.views import AllBlogs, BlogDetailView


urlpatterns = [
    path('', AllBlogs.as_view(), name='allblogs'),
    path('<int:blog_id>/', BlogDetailView.as_view(), name='detail'),
]
