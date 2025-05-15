# Gas Utility Customer Service System

A Django application to manage customer service requests for a gas utility company. Built to improve customer support efficiency and reduce long wait times.

---

##  Features

- Submit and manage gas service requests
- Track request status (submitted, in progress, resolved, closed)
- Staff dashboard to approve/reject requests
- File attachments for issue evidence
- Authentication (login/logout/register)
- Admin panel for staff
- Bulk resolve tool for admins

---

## Tech Stack

- Python 3.12
- Django 4.x
- SQLite (default) or PostgreSQL (optional)
- HTML/CSS (template-based)

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   https://github.com/dhaneshredd6/Django-Gas-Utility-App.git
   cd gas-utility-system
   
2.**Create and activate a virtual environment**
  python -m venv env
  source env/bin/activate   # On Windows: env\Scripts\activate
  
3.**Install requirements**
 pip install -r requirements.txt
 
4.**Run migrations
 python manage.py makemigrations
 python manage.py migrate
 
5.**Create superuser
python manage.py createsuperuser

6.**Start development server
 python manage.py runserver


🔐 Admin Tools
Login to /admin/ with superuser credentials

Mark users as "staff" to access /staff/dashboard/

Approve/reject requests individually or use bulk actions

📁 Project Structure

    project/
│
├── services/               # Main app
│   ├── admin.py            # Admin interface for staff
│   ├── models.py           # ServiceRequest model
│   ├── views.py            # Views for user/staff dashboards
│   ├── urls.py             # App URLs
│   └── templates/
│       ├── dashboard.html          # User dashboard
│       └── staff_dashboard.html    # Staff-only dashboard
│
├── static/                # Static files (CSS/JS)
├── templates/             # Global templates
├── db.sqlite3             # Database
└── manage.py

#Technologies Used

Django 5.2

SQLite3

HTML5 + CSS

Optional file attachment support

Simple role-based access logic

📌 Notes

Make sure you have staff_dashboard.html under services/templates/

You must be logged in as a staff user to access the staff dashboard

This project fulfills the key goals of the assignment:

✅ Handles large volume of customer requests

✅ Enables full tracking lifecycle

✅ Provides support tools for agents

✅ Follows clean and modular Django structure


✅ Used custom dashboards with real-time counters

✅ Followed modular and readable app structure

✅ Included both staff and customer perspectives









