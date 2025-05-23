from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

from .models import Book


def index(request):
    return redirect('catalog')

def show_catalog(request):
    sort = request.GET.get('sort', '')

    if sort == 'title':
        books = Book.objects.all().order_by('title')
    elif sort == 'min_price':
        books = Book.objects.all().order_by('price')
    elif sort == 'max_price':
        books = Book.objects.all().order_by('-price')
    else:
        books = Book.objects.all()

    template = 'catalog.html'
    context = {'books': books}
    return render(request, template, context)

def details(request, book_id):
    try:
        book = Book.objects.get(id = book_id)

        template_name = "product.html"
        return render(request, template_name, {"book": book})
    except Book.DoesNotExist:
        raise Http404("Товар не найден")

def hello(request):
    return HttpResponse("TEST_CI/CD")