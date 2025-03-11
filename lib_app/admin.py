from django.contrib import admin
from .models import Book1, Borrower, BookBorrowing

@admin.register(Book1)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'is_available')
    search_fields = ('title', 'author', 'isbn')

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

@admin.register(BookBorrowing)
class BookBorrowingAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'borrow_date', 'return_date', 'is_returned')
    list_filter = ('is_returned',)
    search_fields = ('book__title', 'borrower__name')
