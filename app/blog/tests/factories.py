from factory.django import DjangoModelFactory
from blog.models import Blog


class BlogFactory(DjangoModelFactory):
    class Meta:
        model = Blog
