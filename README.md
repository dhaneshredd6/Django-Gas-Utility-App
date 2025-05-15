# Gas Utility Customer Service System

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-lightgray.svg)](https://www.sqlite.org/index.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) A Django application designed to streamline customer service for gas utility companies. This system aims to enhance support efficiency and significantly reduce customer wait times by providing a user-friendly platform for submitting and managing service requests.

## ✨ Features

- **Submit and Manage Gas Service Requests:** Customers can easily submit new service requests with relevant details.
- **Track Request Status:** Real-time updates on the status of service requests (Submitted, In Progress, Resolved, Closed).
- **Staff Dashboard:** A dedicated dashboard for staff members to review, approve, and reject customer requests.
- **File Attachments:** Option for users to attach relevant files (e.g., images, documents) to their service requests for better issue evidence.
- **Authentication:** Secure user authentication system with login, logout, and registration functionalities.
- **Admin Panel:** Django's built-in admin interface for managing staff users and system configurations.
- **Bulk Resolve Tool:** Administrators have access to a tool for resolving multiple requests efficiently.

## 🛠️ Tech Stack

This project is built using the following technologies:

- **Backend:**
    - [Python 3.12](https://www.python.org/downloads/release/python-3120/)
    - [Django 5.2](https://www.djangoproject.com/)
    - Database:
        - [SQLite](https://www.sqlite.org/index.html) (Default)
        - [PostgreSQL](https://www.postgresql.org/) (Optional)
- **Frontend:**
    - HTML5
    - CSS (Template-based)

## ⚙️ Setup Instructions

Follow these steps to get the application running on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/dhaneshredd6/Django-Gas-Utility-App.git](https://github.com/dhaneshredd6/Django-Gas-Utility-App.git)
   cd gas-utility-system

   Create and activate a virtual environment:

Bash

python -m venv env
source env/bin/activate  # On Linux/macOS
env\Scripts\activate   # On Windows
Install dependencies:

 -Bash

-pip install -r requirements.txt
-Run database migrations:

Bash

python manage.py makemigrations
python manage.py migrate
Create a superuser (admin account):

Bash

python manage.py createsuperuser
Follow the prompts to create your admin username, email, and password.

Start the development server:

Bash

python manage.py runserver
The application will be accessible 1  at http://127.0.0.1:8000/.   
 1. 
github.com
github.com

🔑 Accessing Admin and Staff Tools
Admin Panel: Navigate to http://127.0.0.1:8000/admin/ and log in using the superuser credentials you created. Here, you can manage users and other administrative tasks.

Staff Dashboard:

Log in to the admin panel (/admin/).
Find the user you want to grant staff access.
Check the "Staff status" box and save the user.
Staff users can then access the staff dashboard at http://127.0.0.1:8000/staff/dashboard/.
📂 Project Structure
project/
├── services/                 # Main application logic
│   ├── admin.py              # Admin interface customizations for staff
│   ├── models.py             # Defines the ServiceRequest data model
│   ├── views.py              # Handles the logic for user and staff dashboards
│   ├── urls.py               # Defines the URL patterns for the 'services' app
│   └── templates/          # HTML templates for the 'services' app
│       ├── dashboard.html    # Template for the user dashboard
│       └── staff_dashboard.html # Template for the staff-only dashboard
│   └── static/               # Static files (CSS, JavaScript) for the 'services' app
├── templates/                # Global HTML templates for the project
├── db.sqlite3                # Default SQLite database file
└── manage.py                 # Django management script
📌 Important Notes
Ensure that the staff_dashboard.html file is located within the services/templates/ directory.
Access to the staff dashboard (/staff/dashboard/) is restricted to users with staff status. You need to mark users as "staff" in the Django admin panel.
✅ Project Goals Achieved
This project successfully addresses the key objectives of the assignment:

✅ Handles a large volume of customer requests effectively.
✅ Enables a complete tracking lifecycle for service requests.
✅ Provides dedicated support tools for agents through the staff dashboard.
✅ Follows a clean and modular Django project structure.
✅ Implements custom dashboards with real-time counters (implementation details in views.py and templates).
✅ Maintains a modular and readable application structure within the services app.
✅ Incorporates both staff and customer perspectives through separate dashboards and functionalities.
