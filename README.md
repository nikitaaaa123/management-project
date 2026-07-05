
```markdown
# 📋 Task Management System

A responsive, full-stack **Task Management System** built using HTML5, CSS3, JavaScript, Python (Flask), and MySQL. This application allows administrators and managers to securely log in, assign tasks to team members, track completion status, and monitor team efficiency through a live metrics dashboard.

---

## 🚀 Key Features & Modules

* **🔒 Authentication Module:** Secure role-based login system restricted to `admin` and `manager` roles. Protects dashboard routes and manages user sessions.
* **📊 Live Metrics Dashboard:** Real-time statistics counter displaying **Total Assigned**, **Pending Completion**, and **Completed** tasks directly at the top of the workspace.
* **👥 Employee & Task Management:** Simple form assignment linking employees to standardized task categories with initial boolean status selection (`True` / `False`).
* **🎨 Modern UI/UX Design:** Built with glassmorphism styling, soft shadows, responsive CSS Grid layout, interactive hover transitions, and auto-dismissing notification alerts.
* **🛡️ Crash-Resistant Database Integration:** Uses **PyMySQL** and environment variables (`.env`) for seamless, secure, and crash-free MySQL connectivity across Windows, macOS, and Linux environments.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, Custom Modern CSS (Variables, Grid, Flexbox), JavaScript (DOM manipulation & form validation)
* **Backend:** Python 3, Flask Web Framework
* **Database:** MySQL / MariaDB
* **Database Driver:** PyMySQL (Pure-Python MySQL client for enhanced OS stability)
* **Configuration:** `python-dotenv` for secure environment variable management

---

## ⚙️ Setup & Installation Instructions

### 1. Database Setup
1. Open your MySQL command line, phpMyAdmin, or MySQL Workbench.
2. Run the provided SQL script to create the database, tables, and default test data:
   ```sql
   SOURCE database.sql;

```

*(Alternatively, copy and paste the contents of `database.sql` into your SQL query execution tab and execute it).*

### 2. Install Python Dependencies

Open your terminal or command prompt inside the project folder and install the required packages:

```bash
pip install -r requirements.txt

```

Ensure your **`requirements.txt`** contains the following specifications:

```text
Flask==3.0.3
pymysql==1.1.1
python-dotenv==1.0.1

```

### 3. Configure Environment Variables (`.env`)

To avoid hardcoding sensitive database passwords, create a new file named exactly **`.env`** in the root project directory and add your local MySQL configuration:

```ini
# Flask Security Key
FLASK_SECRET_KEY="super-secret-key-change-this-in-production"

# MySQL Database Credentials
DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD="your_mysql_password_here"
DB_NAME="task_management_system"

```

* **Important:** Replace `"your_mysql_password_here"` with your actual local MySQL root password. If you are using XAMPP, WAMP, or MAMP where the default root password is empty, set it as `DB_PASSWORD=""`.

### 4. Run the Application

Start the Flask development server from your terminal:

```bash
python app.py

```

Once running, open your web browser and navigate to:

```text
[http://127.0.0.1:5000](http://127.0.0.1:5000)

```

---

## 🔐 Demo Login Credentials

The `database.sql` script creates two default user accounts for initial testing:

| Role | Username | Password |
| --- | --- | --- |
| **Administrator** | `admin` | `admin123` |
| **Manager** | `manager` | `manager123` |

---

## 🗺️ Application Routes

* `GET /` — Login Page (Redirects to `/tasks` if already authenticated)
* `POST /` — Authenticates user credentials against the MySQL `login` table
* `GET /tasks` — Main Task Directory and Live Metrics Dashboard
* `POST /tasks` — Assigns a new task (Validates backend input and updates MySQL)
* `GET /logout` — Clears the user session and redirects to the login screen

---

## 💡 Implementation Notes & Database Integrity

* **No Signup Page:** For security purposes, administrative and managerial accounts can only be created or modified directly within the database by system administrators.
* **Auto-Generated Task IDs:** Task IDs are handled automatically via MySQL's `AUTO_INCREMENT` primary key constraint.
* **Relational Integrity:** The `task` table utilizes a foreign key (`employee_id`) linked directly to the `employee` table with `ON DELETE CASCADE` rules. If an employee record is removed, all associated tasks are cleaned up automatically.
* **Auto-Dismissing Alerts:** Flash notifications (success/error messages) automatically fade out after 4 seconds via custom JavaScript to keep the UI uncluttered.

---

## ❓ Troubleshooting & FAQ

### 1. Why do I get `Access denied for user 'root'@'localhost'`?

This indicates that Flask successfully reached MySQL, but the password provided in your `.env` file does not match your MySQL server's root password. Verify your `.env` file and make sure `DB_PASSWORD="your_actual_password"` is set correctly. **Remember to restart your terminal (`Ctrl + C`, then `python app.py`) whenever you modify the `.env` file.**

### 2. Why does the terminal close or freeze silently when clicking "Sign In" on Windows?

Older native C-based MySQL drivers (like `mysql-connector-python`) can experience C-library segmentation faults on certain Windows and Python configurations. This project uses **`PyMySQL`** (a 100% pure-Python database driver) to completely prevent terminal crashes and ensure cross-platform stability. Ensure you have uninstalled the old connector and installed `pymysql` via `pip`.

```

```
