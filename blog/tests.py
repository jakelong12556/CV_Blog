from django.urls import resolve, path
from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth import views
from blog.views import post_list, post_detail, post_draft_list
from blog.views import post_edit, post_new, post_publish, post_remove


# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_CV_page(self):
        found = resolve('/')
        self.assertEqual(found.func, views.LoginView.as_view())

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Phan Cuong CV Blog</title>', html)
