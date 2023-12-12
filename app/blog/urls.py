from django.urls import path
from blog.views import BlogView, BlogDetailView

urlpatterns = [
    path("blogs/", BlogView.as_view(), name="blogs_page"),
    path("blog/<blog_uid>/", BlogDetailView.as_view(), name="blog_details_page"),
]
