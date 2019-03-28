from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book


@login_required
def book_list_view(request):
    """
    View to render the book_list.html template.
    """
    books = get_list_or_404(
        Book,
        user=request.user.id,
        )
    context = {
        'books': books,
    }

    return render(request, 'books/book_list.html', context)


@login_required
def book_detail_view(request, pk=None):
    """
    View to render the book_details.html template.
    """
    book = get_object_or_404(
        Book,
        id=pk,
        user=request.user.id
        )
    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)
