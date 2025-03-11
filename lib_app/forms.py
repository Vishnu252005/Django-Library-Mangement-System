from django import forms
from .models import Book1, Borrower, BookBorrowing

class BookForm(forms.ModelForm):
    class Meta:
        model = Book1
        fields = ['title', 'author', 'published_date', 'isbn']

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name', 'email', 'phone']

class BookBorrowingForm(forms.ModelForm):
    class Meta:
        model = BookBorrowing
        fields = ['book', 'borrower']
        
class BookReturnForm(forms.Form):
    book_borrowing = forms.ModelChoiceField(
        queryset=BookBorrowing.objects.filter(is_returned=False),
        label="Select book to return"
    )
