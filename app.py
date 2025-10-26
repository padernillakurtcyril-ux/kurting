from flask import Flask, jsonify, request, render_template_string, redirect, url_for

app = Flask(__name__)

# 🧠 Temporary student data (acts like a database)
students = [
    {"id": 1, "name": "Juan Dela Cruz", "grade": 85, "section": "Zechariah"},
    {"id": 2, "name": "Maria Santos", "grade": 90, "section": "Genesis"}
]

# 🌈 Layout Template
layout = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Student API</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #4b6cb7, #182848);
            color: #fff;
            font-family: 'Poppins', sans-serif;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            padding-top: 80px;
        }
        .card {
            background: #fff;
            color: #333;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
            padding: 2rem;
            animation: fadeIn 0.6s ease;
        }
        h2, h3 {
            color: #182848;
            font-weight: 700;
        }
        .btn-custom {
            border: none;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .btn-custom:hover {
            transform: scale(1.05);
        }
        footer {
            text-align: center;
            color: rgba(255,255,255,0.8);
            margin-top: 50px;
            font-size: 14px;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <footer>© 2025 Flask Student API | Built beautifully with ❤️ and Bootstrap</footer>
</body>
</html>
"""

# 🏠 Home Route
@app.route('/')
def home():
    html = """
    {% extends "layout" %}
    {% block content %}
    <div class="card text-center mx-auto" style="max-width: 500px;">
        <h2>Welcome to the Flask Student API 🎓</h2>
        <p class="mt-3">Easily manage student records — add, view, and get JSON data.</p>
        <div class="mt-4">
            <a href="/add_student" class="btn btn-primary btn-custom m-2">➕ Add Student</a>
            <a href="/view_students" class="btn btn-success btn-custom m-2">📋 View Students</a>
        </div>
    </div>
    {% endblock %}
    """
    return render_template_string(html, layout=layout)

# ➕ Add Student
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        grade = int(request.form.get('grade'))
        section = request.form.get('section')

        new_id = len(students) + 1
        students.append({
            "id": new_id,
            "name": name,
            "grade": grade,
            "section": section
        })
        return redirect(url_for('view_students'))

    html = """
    {% extends "layout" %}
    {% block content %}
    <div class="card mx-auto" style="max-width: 500px;">
        <h3>Add New Student 🧑‍🎓</h3>
        <form method="POST" class="mt-3">
            <div class="mb-3">
                <label class="form-label">Name:</label>
                <input type="text" name="name" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Grade:</label>
                <input type="number" name="grade" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Section:</label>
                <input type="text" name="section" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary btn-custom">Add Student</button>
            <a href="/view_students" class="btn btn-secondary btn-custom">Back</a>
        </form>
    </div>
    {% endblock %}
    """
    return render_template_string(html, layout=layout)

# 📋 View All Students
@app.route('/view_students')
def view_students():
    html = """
    {% extends "layout" %}
    {% block content %}
    <div class="card">
        <h3>All Students 📚</h3>
        <table class="table table-striped mt-3">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Grade</th>
                    <th>Section</th>
                </tr>
            </thead>
            <tbody>
                {% for s in students %}
                <tr>
                    <td>{{ s.id }}</td>
                    <td>{{ s.name }}</td>
                    <td>{{ s.grade }}</td>
                    <td>{{ s.section }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <a href="/" class="btn btn-outline-primary btn-custom mt-3">🏠 Back to Home</a>
    </div>
    {% endblock %}
    """
    return render_template_string(html, layout=layout, students=students)

# 🔍 Single Student API (JSON)
@app.route('/student/<int:id>')
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student)

# 🚀 Run app
if __name__ == '__main__':
    app.run(debug=True)
