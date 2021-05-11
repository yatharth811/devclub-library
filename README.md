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

# Note

- Create a new user for yourself while running this program and give librarian status to it to get a better understanding of the project.
- Few Features have not been implemented like verification on sign-up.
- To test the emails on sign up and forgot password update following variables in settings.py in 'home' folder. (Email ID used before got banned after submission (29-04-2021).)

    `EMAIL_HOST_USER = "<email-id-from-which-you-will-receive-mails>"`

    `EMAIL_HOST_PASSWORD = "<password>"`
