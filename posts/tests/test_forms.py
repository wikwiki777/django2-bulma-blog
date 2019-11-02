from django.test import TestCase
from django.core import mail
from posts import forms


# class TestForm(TestCase):
#     def test_valid_blog_post_form_creation(self):
#         form = forms.Post(request.POST)({
#             'title': "The is the title of the blog post",
#             'content': "This is the content of the blog post",
#             'image': "BlogPostImage.png",
#             'tag': "Test",
#             'published_date': "2011-09-01T13:20:30+03:00"})
#         self.assertTrue(form.is_valid())

    # def test_invalid_contact_us_form(self):
    #     form = forms.ContactForm({
    #         'message': "Hi there"})
    #     self.assertFalse(form.is_valid())
