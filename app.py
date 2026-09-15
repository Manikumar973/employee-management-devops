from flask import Flask, render_template, request, redirect
from database import create_table, get_db_connection

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Health Check
@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "Employee Management",
        "message": "Application is running successfully"
    }


# Add Employee
@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO employees (name, email, department, salary)
            VALUES (?, ?, ?, ?)
            """,
            (name, email, department, salary)
        )

        connection.commit()
        connection.close()

        return redirect("/employees")

    return render_template("add_employee.html")


# View Employees
@app.route("/employees")
def employees():

    connection = get_db_connection()

    employee_list = connection.execute(
        "SELECT * FROM employees"
    ).fetchall()

    connection.close()

    return render_template(
        "employees.html",
        employees=employee_list
    )


# Edit Employee
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):

    connection = get_db_connection()

    employee = connection.execute(
        "SELECT * FROM employees WHERE id = ?",
        (id,)
    ).fetchone()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        salary = request.form["salary"]

        connection.execute(
            """
            UPDATE employees
            SET name = ?, email = ?, department = ?, salary = ?
            WHERE id = ?
            """,
            (name, email, department, salary, id)
        )

        connection.commit()
        connection.close()

        return redirect("/employees")

    connection.close()

    return render_template(
        "edit_employee.html",
        employee=employee
    )


# Delete Employee
@app.route("/delete/<int:id>")
def delete_employee(id):

    connection = get_db_connection()

    connection.execute(
        "DELETE FROM employees WHERE id = ?",
        (id,)
    )

    connection.commit()
    connection.close()

    return redirect("/employees")


# Start Application
if __name__ == "__main__":
    create_table()
    app.run(host="0.0.0.0", port=5000)