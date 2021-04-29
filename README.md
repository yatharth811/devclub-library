# devclub-library
Library Management System implemented using Django Framework.

# Features
- Three Different types of users : Admin, Librarian and Student
- Users can request for password change through mail by using Forget Password.
- Welcome Emails to newly registered users.
- Login also possible through Github.
- Search Books by Title
- Librarian can add book, edit book details and students can request books (if available).
- Librarians can respond to issue requests by students

# Requirements
- Python

# Installation
- Install django using `pip install django` (if not installed)
- Run `python manage.py runserver`

# Accounts

| USERNAME | PASSWORD | PRIVILEGE |
| -------- | -------- | --------- |
| admin    |pass@1234 | admin+librarian | 
| rickandmorty |  pass@1234  | student |
| scoobydoo | pass@1234 | student |
