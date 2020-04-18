from django.urls import path
from blog.views import Allblogs, BlogDetailView


urlpatterns = [
    path('', Allblogs.as_view(), name='allblogs'),
    path('<int:blog_id>/', BlogDetailView.as_view(), name='detail'),
]
