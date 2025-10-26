from flask import Flask, jsonify, request, render_template_string, redirect, url_for

app = Flask(__name__)

# --- In-memory list (temporary database) ---
students = [
    {"id": 1, "name": "Juan Dela Cruz", "grade": 90, "section": "Zechariah"},
    {"id": 2, "name": "Maria Santos", "grade": 85, "section": "Zion"}
]

# --- Base HTML Layout (applied to all pages) ---
layout = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Student System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #4b6cb7, #182848);
            color: #fff;
            font-family: 'Poppins', sans-serif;
            min-height: 100vh;
            margin: 0;
        }
        .navbar {
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
        }
        .navbar a { color: white !important; font-weight: 500; }
        .card {
            background: #ffffff;
            color: #333;
            border: none;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            padding: 2rem;
            animation: fadeIn 0.7s ease;
        }
        footer {
            margin-top: 40px;
            text-align: center;
            color: rgba(255,255,255,0.8);
            font-size: 14px;
        }
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(10px);}
            to {opacity: 1; transform: translateY(0);}
        }
    </style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark px-3">
    <a class="navbar-brand" href="/">🎓 Flask Student System</a>
    <div class="navbar-nav ms-auto">
        <a class="nav-link" href="/">Home</a>
        <a class="nav-link" href="/add_student">Add Student</a>
        <a class="nav-link" href="/view_students">View Students</a>
    </div>
</nav>

<div class="container my-5">
    {% block content %}{% endblock %}
</div>

<footer>© 2025 Flask Student API | Built with ❤️ Flask & Bootstrap</footer>
</body>
</html>
"""

# --- HOME PAGE ---
@app.route('/')
def home():
    html = """
    {% extends "layout" %}
    {% block content %}
    <div class="card text-center mx-auto" style="max-width: 500px;">
        <h2>Welcome to the Flask Student API 🎓</h2>
        <p class="mt-3">Easily manage student records — add, view, and analyze.</p>
        <div class="mt-4">
            <a href="/add_student" class="btn btn-primary m-2">➕ Add Student</a>
            <a href="/view_students" class="btn btn-success m-2">📋 View Students</a>
        </div>
    </div>
    {% endblock %}
    """
    return render_template_string(html, layout=layout)

# --- ADD STUDENT ---
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        grade = int(request.form['grade'])
        section = request.form['section']
        new_id = max([s['id'] for s in students]) + 1 if students else 1
        students.append({"id": new_id, "name": name, "grade": grade, "section": section})
        return redirect(url_for('view_students'))

    html = """
    {% extends "layout" %}
    {% block content %}
    <div class="card mx-auto" style="max-width: 500px;">
        <h3 class="text-center mb-3">➕ Add New Student</h3>
        <form method="POST">
            <div class="mb-3">
                <label class="form-label">Full Name</label>
                <input type="text" class="form-control" name="name" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Grade</label>
                <input type="number" class="form-control" name="grade" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Section</label>
                <input type="text" class="form-control" name="section" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">Add Student</button>
        </form>
    </div>
    {% endblock %}
    """
    return render_template_string(html, layout=layout)

# --- VIEW ALL STUDENTS ---
@app.route('/view_students')
def view_students():
    html = """
    {% extends "layout" %}
    {% block content %}
    <div class="card">
        <h3 class="mb-4 text-center">📋 Student List</h3>
        <table class="table table-hover">
            <thead class="table-primary">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Grade</th>
                    <th>Section</th>
                    <th>Remarks</th>
                </tr>
            </thead>
            <tbody>
                {% for s in students %}
                <tr>
                    <td>{{ s.id }}</td>
                    <td>{{ s.name }}</td>
                    <td>{{ s.grade }}</td>
                    <td>{{ s.section }}</td>
                    <td>
                        {% if s.grade >= 75 %}
                        <span class="badge bg-success">Pass</span>
                        {% else %}
                        <span class="badge bg-danger">Fail</span>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <div class="text-center mt-3">
            <a href="/add_student" class="btn btn-primary">Add Another Student</a>
        </div>
    </div>
    {% endblock %}
    """
    return render_template_string(html, layout=layout, students=students)

# --- API ENDPOINT (JSON DATA) ---
@app.route('/api/students')
def api_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
