from django.http import HttpResponse
from p_library.models import Book
from p_library.models import PublishingHouse
from django.template import loader
from django.shortcuts import redirect


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {"title": "мою библиотеку",
                   "books":books,
                    }
    return HttpResponse(template.render(biblio_data, request))

def pub(request):
    template = loader.get_template('pub.html')
    publishinghouses = PublishingHouse.objects.all()
    publishing_data = {
        "publishinghouses":publishinghouses,
    }
    return HttpResponse(template.render(publishing_data, request))