from django.views.generic import ListView

# Create your views here.
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    content_object_name = 'my_list_of_books'
