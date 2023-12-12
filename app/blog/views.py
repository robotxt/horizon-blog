from django.views.generic import ListView
from blog.models import Blog
from django.views.generic import TemplateView


class BlogView(ListView):
    context_object_name = "blogs"
    queryset = Blog.objects.all().exclude(published_date=None)
    template_name = "blog.html"
