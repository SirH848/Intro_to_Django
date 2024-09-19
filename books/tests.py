from django.test import TestCase
from django.urls import reverse
from .models import Book

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='My title',
            subtitle='My subtitle',
            author='Tom and Jerry',
            isbn='123456789123'
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'My title')
        self.assertEqual(self.book.subtitle, 'My subtitle')
        self.assertEqual(self.book.author, 'Tom and Jerry')
        self.assertEqual(self.book.isbn, '123456789123')
    
    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My subtitle')
        self.assertTemplateUsed(response, 'books/book_list.html')