# dev_assignment

I haven't deployed on Heroku. The local versioncan be started by `python manage.py runserver` after creating a venv and installing requirements.txt as instructed in the readme of Assignment 5.

## General Features

- Django
- Has a registration system
- Has 3 kind of accounts - admin is superuser, staff is by a group uses the default admin page for many funtions and user is normal user, the accounts as per instructions have been created.
- staff can do some changes using admin page but I have created a filter which is used in Navbar so that Bookings of slots can be seen by staff only from there.
- Each sport has its own page
- Have limited booking slots to 3 per user per day, haven't tested this much though.
- Acceptance of requests is automatic
