from django.test import TestCase

# Create django tests here.
class TestTonyBlogs(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)
class TestBlogs(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_blog(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_blog_post(self):
        response = self.client.get('/blog/post/')
        self.assertEqual(response.status_code, 200)

class TestBlog(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_aboutpage(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_blogpage(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_contactpage(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_createpage(self):
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_loginpage(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_postpage(self):
        response = self.client.get('/blog/post/1/')
        self.assertEqual(response.status_code, 200)

    def test_profilepage(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_registerpage(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_searchpage(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)

# Create your tests here.

# To run tests: python manage.py test tony_blogs
