# Library Management System

A Django-based Library Management System that helps track books, borrowers, and book borrowings.

## Features

- Book Management (Add, Edit, List books)
- Borrower Management (Add and List borrowers)
- Borrowing System (Borrow and Return books)
- Track book availability
- Detailed borrowing history
- Admin interface for database management

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd Library_Management_System
   ```

2. **Create Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # For Windows:
   .\venv\Scripts\activate
   # For Linux/Mac:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django==5.1.5
   ```

4. **Apply Database Migrations**
   ```bash
   # Create migrations
   python manage.py makemigrations

   # Apply migrations
   python manage.py migrate
   ```

5. **Create Superuser (Admin Account)**
   ```bash
   python manage.py createsuperuser
   # Enter the following credentials when prompted:
   # Username: vishn
   # Password: 1234
   # Email: (can be left blank)
   # Note: When it warns about password being too short/common, type 'y' to use it anyway
   ```

   Default Admin Credentials:
   - Username: vishn
   - Password: 1234

## Running the Application

1. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

2. **Access the Application**
   - Main Site: http://127.0.0.1:8000/
   - Admin Interface: http://127.0.0.1:8000/admin

## Application Structure

- `/lib_app` - Main application directory
  - `models.py` - Database models (Book, Borrower, BookBorrowing)
  - `views.py` - View functions
  - `forms.py` - Form definitions
  - `admin.py` - Admin interface configuration
  - `/templates` - HTML templates

## Available URLs

- `/` - Home page
- `/book_list/` - List of all books
- `/add/` - Add new book
- `/edit/<id>/` - Edit existing book
- `/add_borrower/` - Add new borrower
- `/borrower_list/` - List of all borrowers
- `/borrow_book/` - Record a book borrowing
- `/return_book/` - Record a book return
- `/borrowing_list/` - View all borrowing records

## Database Management

1. **Using Admin Interface (Recommended)**
   - Go to http://127.0.0.1:8000/admin
   - Log in with superuser credentials
   - Manage Books, Borrowers, and Borrowing records

2. **Using Django Shell**
   ```python
   python manage.py shell
   
   # Example queries:
   from lib_app.models import Book1, Borrower, BookBorrowing
   
   # View all books
   Book1.objects.all()
   
   # View all borrowers
   Borrower.objects.all()
   
   # View borrowing history
   BookBorrowing.objects.all()
   ```

## Models

1. **Book1**
   - title (CharField)
   - author (CharField)
   - published_date (DateField)
   - isbn (CharField, unique)
   - is_available (BooleanField)

2. **Borrower**
   - name (CharField)
   - email (EmailField)
   - phone (CharField)

3. **BookBorrowing**
   - book (ForeignKey to Book1)
   - borrower (ForeignKey to Borrower)
   - borrow_date (DateTimeField)
   - return_date (DateTimeField)
   - is_returned (BooleanField)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
