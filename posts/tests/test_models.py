from django.test import TestCase
from posts.models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Post.objects.create(title="Test Post",
                            content="This is a test blogpost",
                            created_date="ljj")

    def test_title_label(self):
        title = Post.objects.first()
        field_label = title._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        title = Post.objects.first()
        max_length = title._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_content_label(self):
        content = Post.objects.first()
        field_label = content._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_created_date_label(self):
        created_date = Post.objects.first()
        field_label = created_date._meta.get_field('created_date').verbose_name
        self.assertEqual(field_label, 'created date')

    def test_published_date_label(self):
        published_date = Post.objects.first()
        field_label = published_date._meta.get_field("published_date").verbose_name
        self.assertEqual(field_label, 'published date')

    def test_views_label(self):
        views = Post.objects.first()
        field_label = views._meta.get_field('views').verbose_name
        self.assertEqual(field_label, 'views')

    def test_tag_label(self):
        tag = Post.objects.first()
        field_label = tag._meta.get_field('tag').verbose_name
        self.assertEqual(field_label, 'tag')

    def test_image_label(self):
        image = Post.objects.first()
        field_label = image._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')
