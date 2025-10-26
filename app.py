from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

# === In-memory database (temporary; resets when app restarts) ===
students = [
    {"id": 1, "name": "Juan Dela Cruz", "grade": 10, "section": "Zechariah"},
    {"id": 2, "name": "Maria Santos", "grade": 9, "section": "Gabriel"}
]
next_id = 3

# === Global CSS Style (applied to all pages) ===
base_style = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    body {
        background: linear-gradient(120deg, #4b6cb7, #182848);
        font-family: 'Poppins', sans-serif;
        color: #fff;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .container {
        background: rgba(255,255,255,0.97);
        color: #333;
        border-radius: 20px;
        padding: 2rem 2.5rem;
        margin-top: 3rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        max-width: 700px;
        width: 90%;
        animation: fadeUp 0.8s ease;
    }
    h1 {
        font-weight: 700;
        color: #182848;
        text-align: center;
        margin-bottom: 1rem;
    }
    a.btn-custom, button.btn-custom {
        background: linear-gradient(135deg, #4b6cb7, #182848);
        color: #fff !important;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    a.btn-custom:hover, button.btn-custom:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 18px rgba(0,0,0,0.3);
    }
    .table {
        border-radius: 10px;
        overflow: hidden;
    }
    .table th {
        background: #4b6cb7;
        color: white;
    }
    footer {
        color: rgba(255,255,255,0.8);
        margin-top: auto;
        text-align: center;
        padding: 15px 0;
    }
    @keyframes fadeUp {
        from {opacity: 0; transform: translateY(30px);}
        to {opacity: 1; transform: translateY(0);}
    }
</style>
"""

# === HOME PAGE ===
@app.route('/')
def home():
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head><title>Flask Student API</title>{base_style}</head>
    <body>
        <div class="container text-center">
            <h1>🎓 Flask Student API</h1>
            <p>Manage student data with CRUD functionality and API support.</p>
            <a href="/students" class="btn btn-custom m-2">📋 View Students</a>
            <a href="/add" class="btn btn-custom m-2">➕ Add Student</a>
            <a href="/api/students" class="btn btn-custom m-2">🌐 View JSON API</a>
        </div>
        <footer>© 2025 Flask Student API • Crafted with 💙 using Bootstrap</footer>
    </body>
    </html>
    """
    return render_template_string(html)

# === VIEW STUDENTS PAGE ===
@app.route('/students')
def view_students():
    rows = ""
    for s in students:
        rows += f"""
        <tr>
            <td>{s['id']}</td>
            <td>{s['name']}</td>
            <td>{s['grade']}</td>
            <td>{s['section']}</td>
            <td>
                <a href='/edit/{s['id']}' class='btn btn-sm btn-warning me-2'>✏️ Edit</a>
                <a href='/delete/{s['id']}' class='btn btn-sm btn-danger'>🗑 Delete</a>
            </td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head><title>Students</title>{base_style}</head>
    <body>
        <div class="container">
            <h1>📋 Student List</h1>
            <table class="table table-striped table-hover mt-3">
                <thead>
                    <tr>
                        <th>ID</th><th>Name</th><th>Grade</th><th>Section</th><th>Actions</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
            <div class="text-center">
                <a href="/add" class="btn btn-custom mt-3">➕ Add Student</a>
                <a href="/" class="btn btn-secondary mt-3">🏠 Back to Home</a>
            </div>
        </div>
        <footer>© 2025 Flask Student API</footer>
    </body>
    </html>
    """
    return render_template_string(html)

# === ADD STUDENT PAGE ===
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    global next_id
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        section = request.form['section']
        students.append({
            "id": next_id,
            "name": name,
            "grade": int(grade),
            "section": section
        })
        next_id += 1
        return redirect(url_for('view_students'))

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head><title>Add Student</title>{base_style}</head>
    <body>
        <div class="container">
            <h1>➕ Add New Student</h1>
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
                <button type="submit" class="btn btn-custom">Add Student</button>
                <a href="/students" class="btn btn-secondary">Cancel</a>
            </form>
        </div>
        <footer>© 2025 Flask Student API</footer>
    </body>
    </html>
    """
    return render_template_string(html)

# === EDIT STUDENT PAGE ===
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        return "Student not found", 404

    if request.method == 'POST':
        student['name'] = request.form['name']
        student['grade'] = int(request.form['grade'])
        student['section'] = request.form['section']
        return redirect(url_for('view_students'))

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head><title>Edit Student</title>{base_style}</head>
    <body>
        <div class="container">
            <h1>✏️ Edit Student</h1>
            <form method="POST">
                <div class="mb-3">
                    <label class="form-label">Full Name</label>
                    <input type="text" class="form-control" name="name" value="{student['name']}" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Grade</label>
                    <input type="number" class="form-control" name="grade" value="{student['grade']}" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Section</label>
                    <input type="text" class="form-control" name="section" value="{student['section']}" required>
                </div>
                <button type="submit" class="btn btn-custom">Save Changes</button>
                <a href="/students" class="btn btn-secondary">Cancel</a>
            </form>
        </div>
        <footer>© 2025 Flask Student API</footer>
    </body>
    </html>
    """
    return render_template_string(html)

# === DELETE STUDENT FUNCTION ===
@app.route('/delete/<int:id>')
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return redirect(url_for('view_students'))

# === API ENDPOINT (JSON) ===
@app.route('/api/students')
def api_students():
    return jsonify(students)

# === RUN APP ===
if __name__ == '__main__':
    app.run(debug=True)
