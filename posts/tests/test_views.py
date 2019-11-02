from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class TestPage(TestCase):

    def test_home_page_works(self):
        response = self.client.get(reverse("get_posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogposts.html")
        self.assertContains(response, 'Django2-bulma-blog')
