import logging
from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from blog.tests.factories import BlogFactory
from django.test import Client
from django.urls import reverse

logger = logging.getLogger(__name__)


class TestAuthAPI(TestCase):

    def setUp(self) -> None:
        now_date = timezone.now()

        # blog_one is published yesterday
        self.blog_one = BlogFactory.create(
            title="title 1",
            content="content 1",
            published_date=now_date - timedelta(days=1)
        )

        # blog_two is published today
        self.blog_two = BlogFactory.create(
            title="title 2",
            content="content 2",
            published_date=now_date
        )

    def test_valid_login(self):
        client = Client()
        response = client.get(
            reverse("blogs_page"),
        )

        self.assertEqual(200, response.status_code)

        # test blog response order and titles
        default_order = [self.blog_two.title, self.blog_one.title]  # default blog order base on published date
        blogs = response.context["blogs"]
        result_order = [blogs[0].title, blogs[1].title]
        self.assertEqual(default_order, result_order)
