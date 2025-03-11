"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lib_app.views import (
    book_list, add_book, edit_book, home_view,
    add_borrower, borrower_list, borrow_book,
    return_book, borrowing_list
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), 
    path('book_list/', book_list, name='book_list'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('add_borrower/', add_borrower, name='add_borrower'),
    path('borrower_list/', borrower_list, name='borrower_list'),
    path('borrow_book/', borrow_book, name='borrow_book'),
    path('return_book/', return_book, name='return_book'),
    path('borrowing_list/', borrowing_list, name='borrowing_list'),
]
