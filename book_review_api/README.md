# Book Review API

A RESTful API built using Django REST Framework for managing books and reviews.

## Features

- User registration
- JWT authentication
- Browse books
- Add reviews
- Edit and delete reviews
- Change password
- Admin book management

---

## How to Run the Project Locally

```bash
pip install django djangorestframework djangorestframework-simplejwt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
## How to Test Each Endpoint

```bash
Register User
POST /api/register/

Login and Get JWT Token
POST /api/token/

Refresh Token
POST /api/token/refresh/

Change Password
POST /api/change-password/

List Books
GET /api/books/

Get Book Details
GET /api/books/<id>/

Add Book (Admin only)
POST /api/books/

Update Book (Admin only)
PUT /api/books/<id>/

Delete Book (Admin only)
DELETE /api/books/<id>/

Add Review
POST /api/books/<book_id>/reviews/

Get Reviews
GET /api/books/<book_id>/reviews/

Update Review
PUT /api/reviews/<id>/

Delete Review
DELETE /api/reviews/<id>/



