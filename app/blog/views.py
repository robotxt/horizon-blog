from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from blog.models import Blog


class BlogView(ListView):
    context_object_name = "blogs"
    template_name = "blogs.html"

    def get_queryset(self):
        now_date = timezone.now()
        queryset = Blog.objects.filter(published_date__lte=now_date)
        return queryset


class BlogDetailView(ListView):
    template_name = "blog.html"

    def get_queryset(self):
        self.blog = get_object_or_404(Blog, uid=self.kwargs["blog_uid"])
        return self.blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog"] = self.blog
        return context
