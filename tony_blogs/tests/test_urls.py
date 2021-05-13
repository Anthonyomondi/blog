from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tony_blogs.views import index, blog_list, blog_detail, update_view, delete_view, new_blog

# class SimpleTests(SimpleTestCase):
#     def test_home_page_status_code(self):
#         response = self.client.get('/index/')
#         self.assertEqual(response.status_code, 200)

#     def tets_blog_detail_page_status_code(self):
#         response = self.client.get('/blog/')
#         self.assertEqual(response.status_code, 200)


class TestUrls(SimpleTestCase):
    def test_blogs_url_is_resolved(self):
        url = reverse('blogs')
        print(resolve(url))

# class TestUrls(SimpleTestCase):
#     def test_blog_url_is_resolved(self):
#         url = reverse('blog_detail')
#         print(resolve(url))

# class TestUrls(SimpleTestCase):
#     def test_update_url_is_resolved(self):
#         url = reverse('update')
#         print(resolve(url))

# class TestUrls(SimpleTestCase):
#     def test_delete_url_is_resolved(self):
#         url = reverse('delete')
#         print(resolve(url))

# class TestUrls(SimpleTestCase):
#     def test_new_blog_url_is_resolved(self):
#         url = reverse('new_blog')
#         print(resolve(url))