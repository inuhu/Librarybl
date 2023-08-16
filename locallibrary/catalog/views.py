from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic




def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.

    searched_book = Book.objects.filter(title__contains="Война").count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_available': num_instances_available,
                           'num_authors': num_authors,
                           'num_searched_book': searched_book,
                           },
                  )



class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/templates/book_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Books'
        return context



class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/author_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Authors'
        return context


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'
    context_object_name = 'author'

