from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Book1, Borrower, BookBorrowing
from .forms import BookForm, BorrowerForm, BookBorrowingForm, BookReturnForm

def home_view(request):
    """ Renders the home page """
    return render(request, 'home.html')

def add_book(request):
    """ Adds a new book to the database """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_list(request):
    """ Displays the list of books """
    books = Book1.objects.all()
    return render(request, 'book_list.html', {'books': books})

def edit_book(request, book_id):
    """ Edits an existing book """
    book = get_object_or_404(Book1, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def add_borrower(request):
    """ Adds a new borrower """
    if request.method == "POST":
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrower_list')
    else:
        form = BorrowerForm()
    return render(request, 'add_borrower.html', {'form': form})

def borrower_list(request):
    """ Displays the list of borrowers """
    borrowers = Borrower.objects.all()
    return render(request, 'borrower_list.html', {'borrowers': borrowers})

def borrow_book(request):
    """ Records a book borrowing """
    if request.method == "POST":
        form = BookBorrowingForm(request.POST)
        if form.is_valid():
            borrowing = form.save()
            book = borrowing.book
            book.is_available = False
            book.save()
            return redirect('borrowing_list')
    else:
        form = BookBorrowingForm()
        # Only show available books
        form.fields['book'].queryset = Book1.objects.filter(is_available=True)
    return render(request, 'borrow_book.html', {'form': form})

def return_book(request):
    """ Handles book returns """
    if request.method == "POST":
        form = BookReturnForm(request.POST)
        if form.is_valid():
            borrowing = form.cleaned_data['book_borrowing']
            borrowing.return_date = timezone.now()
            borrowing.is_returned = True
            borrowing.save()
            
            book = borrowing.book
            book.is_available = True
            book.save()
            return redirect('borrowing_list')
    else:
        form = BookReturnForm()
    return render(request, 'return_book.html', {'form': form})

def borrowing_list(request):
    """ Displays the list of all borrowings """
    borrowings = BookBorrowing.objects.all().order_by('-borrow_date')
    return render(request, 'borrowing_list.html', {'borrowings': borrowings})
