<h1>Gas Utility Customer Service System</h1>

<p>
  <a href="https://www.python.org/downloads/release/python-3120/">
    <img src="https://img.shields.io/badge/Python-3.12-blue.svg" alt="Python 3.12">
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-5.2-green.svg" alt="Django 5.2">
  </a>
  <a href="https://www.sqlite.org/index.html">
    <img src="https://img.shields.io/badge/SQLite-3-lightgray.svg" alt="SQLite 3">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
</p>

<p>A Django application designed to streamline customer service for gas utility companies. This system aims to enhance support efficiency and significantly reduce customer wait times by providing a user-friendly platform for submitting and managing service requests.</p>

<h2>✨ Features</h2>

<ul>
  <li><strong>Submit and Manage Gas Service Requests:</strong> Customers can easily submit new service requests with relevant details.</li>
  <li><strong>Track Request Status:</strong> Real-time updates on the status of service requests (Submitted, In Progress, Resolved, Closed).</li>
  <li><strong>Staff Dashboard:</strong> A dedicated dashboard for staff members to review, approve, and reject customer requests.</li>
  <li><strong>File Attachments:</strong> Option for users to attach relevant files (e.g., images, documents) to their service requests for better issue evidence.</li>
  <li><strong>Authentication:</strong> Secure user authentication system with login, logout, and registration functionalities.</li>
  <li><strong>Admin Panel:</strong> Django's built-in admin interface for managing staff users and system configurations.</li>
  <li><strong>Bulk Resolve Tool:</strong> Administrators have access to a tool for resolving multiple requests efficiently.</li>
</ul>

<h2>🛠️ Tech Stack</h2>

<ul>
  <li><strong>Backend:</strong>
    <ul>
      <li><a href="https://www.python.org/downloads/release/python-3120/">Python 3.12</a></li>
      <li><a href="https://www.djangoproject.com/">Django 5.2</a></li>
      <li>Database:
        <ul>
          <li><a href="https://www.sqlite.org/index.html">SQLite</a> (Default)</li>
          <li><a href="https://www.postgresql.org/">PostgreSQL</a> (Optional)</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><strong>Frontend:</strong>
    <ul>
      <li>HTML5</li>
      <li>CSS (Template-based)</li>
    </ul>
  </li>
</ul>

<h2>⚙️ Setup Instructions</h2>

<table>
  <tr>
    <td style="width: 40%; vertical-align: top;"><strong>1. Clone the repository:</strong></td>
    <td style="width: 60%; vertical-align: top;">
      <code>
        git clone <a href="https://github.com/dhaneshredd6/Django-Gas-Utility-App.git">https://github.com/dhaneshredd6/Django-Gas-Utility-App.git</a><br>
        cd gas-utility-system
      </code>
    </td>
  </tr>
  <tr>
    <td style="width: 40%; vertical-align: top;"><strong>2. Create and activate a virtual environment:</strong></td>
    <td style="width: 60%; vertical-align: top;">
      <pre><code class="language-bash">
python -m venv env
source env/bin/activate  # On Linux/macOS
env\Scripts\activate    # On Windows
      </code></pre>
    </td>
  </tr>
  <tr>
    <td style="width: 40%; vertical-align: top;"><strong>3. Install dependencies:</strong></td>
    <td style="width: 60%; vertical-align: top;">
      <pre><code class="language-bash">
pip install -r requirements.txt
      </code></pre>
    </td>
  </tr>
  <tr>
    <td style="width: 40%; vertical-align: top;"><strong>4. Run database migrations:</strong></td>
    <td style="width: 60%; vertical-align: top;">
      <pre><code class="language-bash">
python manage.py makemigrations
python manage.py migrate
      </code></pre>
    </td>
  </tr>
  <tr>
    <td style="width: 40%; vertical-align: top;"><strong>5. Create a superuser (admin account):</strong></td>
    <td style="width: 60%; vertical-align: top;">
      <pre><code class="language-bash">
python manage.py createsuperuser
      </code></pre>
      Follow the prompts to create your admin username, email, and password.
    </td>
  </tr>
  <tr>
    <td style="width: 40%; vertical-align: top;"><strong>6. Start the development server:</strong></td>
    <td style="width: 60%; vertical-align: top;">
      <pre><code class="language-bash">
python manage.py runserver
      </code></pre>
    </td>
  </tr>
</table>

<h2>🔑 User Registration and Login</h2>

<ul>
  <li><strong>Registration:</strong> To create a new user account, navigate to <a href="http://127.0.0.1:8000/register/">http://127.0.0.1:8000/register/</a> in your web browser and follow the registration process.</li>
  <li><strong>Login:</strong> Once you have registered, you can log in to your user account by navigating to <a href="http://127.0.0.1:8000/login/">http://127.0.0.1:8000/login/</a> and entering your credentials.</li>
</ul>

<h2>🔑 Accessing Admin and Staff Tools</h2>

<ul>
  <li><strong>Admin Panel:</strong> Navigate to <a href="http://127.0.0.1:8000/admin/">http://127.0.0.1:8000/admin/</a> and log in using the superuser credentials you created. Here, you can manage users and other administrative tasks.</li>
  <li><strong>Staff Dashboard:</strong>
    <ol>
      <li>Log in to the admin panel (<a href="http://127.0.0.1:8000/admin/">/admin/</a>).</li>
      <li>Find the user you want to grant staff access.</li>
      <li>Check the "Staff status" box and save the user.</li>
      <li>Staff users can then access the staff dashboard at <a href="http://127.0.0.1:8000/staff/dashboard/">http://127.0.0.1:8000/staff/dashboard/</a>.</li>
    </ol>
  </li>
</ul>

<h2>📂 Project Structure</h2>

<img src="https://github.com/user-attachments/assets/2e6ac965-55a9-4bcc-94fa-f84daf12d6fd" alt="Project Structure">

<h2>📌 Important Notes</h2>

<ul>
  <li>Ensure that the <code>staff_dashboard.html</code> file is located within the <code>services/templates/</code> directory.</li>
  <li>Access to the staff dashboard (<code>/staff/dashboard/</code>) is restricted to users with staff status. You need to mark users as "staff" in the Django admin panel.</li>
</ul>

<h2>✅ Project Goals Achieved</h2>

<ul>
  <li>✅ Handles a large volume of customer requests effectively.</li>
  <li>✅ Enables a complete tracking lifecycle for service requests.</li>
  <li>✅ Provides dedicated support tools for agents through the staff dashboard.</li>
  <li>✅ Follows a clean and modular Django project structure.</li>
  <li>✅ Implements custom dashboards with real-time counters (implementation details in <code>views.py</code> and templates).</li>
  <li>✅ Maintains a modular and readable application structure within the <code>services</code> app.</li>
  <li>✅ Incorporates both staff and customer perspectives through separate dashboards and functionalities.</li>
</ul>
