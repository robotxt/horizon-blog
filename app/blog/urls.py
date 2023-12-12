from django.urls import path
from blog.views import BlogView, BlogDetailView

urlpatterns = [
    path("blogs/", BlogView.as_view()),
    path("blog/<blog_uid>/", BlogDetailView.as_view()),
]
