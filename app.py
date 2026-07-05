import os
from flask import Flask, redirect, render_template, request, session, url_for
from dotenv import load_dotenv

# PyMySQL Setup
import pymysql
import pymysql.cursors
from pymysql import Error

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "task-management-secret-key-2026")

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "Nikita#06"),
    "database": os.getenv("DB_NAME", "task_management_system"),
}

TASK_TITLES = [
    "Prepare Daily Report",
    "Update Customer Records",
    "Verify Documents",
    "Complete Data Entry",
    "Resolve Support Ticket",
]


def get_connection():
    # PyMySQL connection using DictCursor automatically
    return pymysql.connect(
        **DB_CONFIG, 
        cursorclass=pymysql.cursors.DictCursor
    )


def is_logged_in():
    return "user_id" in session


@app.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        
        if not username or not password:
            return render_template("login.html", error="Please enter both username and password.")

        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()  # Fixed: No (dictionary=True) needed for PyMySQL
            cursor.execute(
                """
                SELECT id, username, role
                FROM login
                WHERE username = %s AND password = %s
                """,
                (username, password),
            )
            user = cursor.fetchone()

            if user and user["role"] in ("admin", "manager"):
                session["user_id"] = user["id"]
                session["username"] = user["username"]
                session["role"] = user["role"]
                return redirect(url_for("task_management"))

            error = "Invalid username, password, or role."
        except Error as exc:
            error = f"Database connectivity error: {exc}"
        finally:
            if cursor:
                cursor.close()
            # Fixed: PyMySQL uses .open instead of .is_connected()
            if conn and conn.open:
                conn.close()

    return render_template("login.html", error=error)


@app.route("/tasks", methods=["GET", "POST"])
def task_management():
    if not is_logged_in():
        return redirect(url_for("login"))

    message = None
    error = None
    employees = []
    tasks = []
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()  # Fixed: Clean PyMySQL cursor

        if request.method == "POST":
            employee_id = request.form.get("employee_id", "").strip()
            title = request.form.get("task_title", "").strip()
            completed_raw = request.form.get("completed", "").strip()

            if not employee_id or not title or completed_raw not in ("true", "false"):
                error = "All form fields are required and must be valid."
            else:
                completed = completed_raw == "true"
                cursor.execute(
                    """
                    INSERT INTO task (employee_id, title, completed)
                    VALUES (%s, %s, %s)
                    """,
                    (int(employee_id), title, completed),
                )
                conn.commit()
                message = "Task successfully assigned!"

        cursor.execute(
            """
            SELECT id, employee_name, department
            FROM employee
            ORDER BY employee_name
            """
        )
        employees = cursor.fetchall()

        cursor.execute(
            """
            SELECT
                task.id AS id,
                task.title AS title,
                task.completed AS completed,
                DATE_FORMAT(task.created_at, '%b %d, %Y - %h:%i %p') AS created_at,
                employee.employee_name,
                employee.department
            FROM task
            JOIN employee ON employee.id = task.employee_id
            ORDER BY task.id DESC
            """
        )
        tasks = cursor.fetchall()

    except Error as exc:
        error = f"Database error: {exc}"
    finally:
        if cursor:
            cursor.close()
        # Fixed: PyMySQL uses .open instead of .is_connected()
        if conn and conn.open:
            conn.close()

    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t["completed"])
    pending_tasks = total_tasks - completed_tasks

    return render_template(
        "tasks.html",
        employees=employees,
        tasks=tasks,
        task_titles=TASK_TITLES,
        message=message,
        error=error,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=True,
    )