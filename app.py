from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# --- Temporary in-memory database ---
students = [
    {"id": 1, "name": "Juan Dela Cruz", "year": "2nd Year", "section": "Zechariah"},
    {"id": 2, "name": "Maria Santos", "year": "1st Year", "section": "Jeremiah"},
    {"id": 3, "name": "Pedro Pascual", "year": "3rd Year", "section": "Daniel"}
]

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Student Manager</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(120deg, #4b6cb7, #182848);
                font-family: 'Poppins', sans-serif;
                color: #fff;
                padding: 3rem 0;
            }
            .container {
                max-width: 950px;
                background: #fff;
                color: #333;
                border-radius: 15px;
                padding: 2.5rem;
                box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            }
            h1 {
                text-align: center;
                font-weight: 700;
                color: #182848;
                margin-bottom: 1.5rem;
            }
            table {
                border-radius: 12px;
                overflow: hidden;
            }
            th {
                background-color: #4b6cb7;
                color: white;
                text-align: center;
            }
            td {
                text-align: center;
                vertical-align: middle;
            }
            .btn-custom {
                background: linear-gradient(135deg, #4b6cb7, #182848);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0.4rem 1rem;
                transition: 0.3s;
            }
            .btn-custom:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 15px rgba(0,0,0,0.3);
                color: #fff;
            }
            form input, form select {
                border-radius: 8px;
            }
            .search-bar input {
                border-radius: 8px;
                padding: 0.6rem 1rem;
            }
            #no-results {
                display: none;
                color: #888;
                text-align: center;
                padding: 1rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎓 Student Manager</h1>

            <!-- Add Student Form -->
            <form action="/add" method="POST" class="mb-4 row g-3 align-items-center">
                <div class="col-md-4">
                    <input type="text" name="name" class="form-control" placeholder="Full Name" required>
                </div>
                <div class="col-md-3">
                    <select name="year" class="form-select" required>
                        <option value="">Select Year</option>
                        <option>1st Year</option>
                        <option>2nd Year</option>
                        <option>3rd Year</option>
                        <option>4th Year</option>
                    </select>
                </div>
                <div class="col-md-3">
                    <input type="text" name="section" class="form-control" placeholder="Section" required>
                </div>
                <div class="col-md-2 text-end">
                    <button type="submit" class="btn btn-custom w-100">Add</button>
                </div>
            </form>

            <!-- Search Bar -->
            <div class="search-bar mb-4">
                <div class="input-group">
                    <input type="text" id="searchInput" class="form-control" placeholder="🔍 Search by name, year, or section...">
                </div>
            </div>

            <!-- Student Table -->
            <table class="table table-bordered table-hover align-middle" id="studentTable">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Full Name</th>
                        <th>Year</th>
                        <th>Section</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {% for student in students %}
                    <tr>
                        <td>{{ student.id }}</td>
                        <td>{{ student.name }}</td>
                        <td>{{ student.year }}</td>
                        <td>{{ student.section }}</td>
                        <td>
                            <a href="/edit/{{ student.id }}" class="btn btn-sm btn-warning">Edit</a>
                            <a href="/delete/{{ student.id }}" class="btn btn-sm btn-danger" onclick="return confirm('Delete this student?')">Delete</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
            <div id="no-results">No students found.</div>
        </div>

        <script>
        // Real-time search filtering
        document.getElementById('searchInput').addEventListener('keyup', function() {
            const query = this.value.toLowerCase();
            const rows = document.querySelectorAll('#studentTable tbody tr');
            let visibleCount = 0;

            rows.forEach(row => {
                const text = row.innerText.toLowerCase();
                if (text.includes(query)) {
                    row.style.display = '';
                    visibleCount++;
                } else {
                    row.style.display = 'none';
                }
            });

            document.getElementById('no-results').style.display = visibleCount ? 'none' : 'block';
        });
        </script>
    </body>
    </html>
    """
    return render_template_string(html, students=students)

@app.route('/add', methods=['POST'])
def add_student():
    new_id = students[-1]['id'] + 1 if students else 1
    new_student = {
        "id": new_id,
        "name": request.form['name'],
        "year": request.form['year'],
        "section": request.form['section']
    }
    students.append(new_student)
    return redirect(url_for('home'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = next((s for s in students if s["id"] == id), None)
    if not student:
        return redirect(url_for('home'))

    if request.method == 'POST':
        student["name"] = request.form["name"]
        student["year"] = request.form["year"]
        student["section"] = request.form["section"]
        return redirect(url_for('home'))

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Edit Student</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(120deg, #4b6cb7, #182848);
                font-family: 'Poppins', sans-serif;
                color: #fff;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .card {
                background: #fff;
                color: #333;
                border-radius: 12px;
                padding: 2rem;
                box-shadow: 0 10px 25px rgba(0,0,0,0.3);
                width: 400px;
            }
            h2 {
                text-align: center;
                font-weight: 700;
                color: #182848;
                margin-bottom: 1rem;
            }
            .btn-custom {
                background: linear-gradient(135deg, #4b6cb7, #182848);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0.5rem 1.5rem;
                width: 100%;
                transition: 0.3s;
            }
            .btn-custom:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 15px rgba(0,0,0,0.3);
                color: #fff;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Edit Student</h2>
            <form method="POST">
                <div class="mb-3">
                    <label class="form-label">Full Name</label>
                    <input type="text" name="name" class="form-control" value="{{ student.name }}" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Year</label>
                    <select name="year" class="form-select" required>
                        <option {{ 'selected' if student.year == '1st Year' else '' }}>1st Year</option>
                        <option {{ 'selected' if student.year == '2nd Year' else '' }}>2nd Year</option>
                        <option {{ 'selected' if student.year == '3rd Year' else '' }}>3rd Year</option>
                        <option {{ 'selected' if student.year == '4th Year' else '' }}>4th Year</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label class="form-label">Section</label>
                    <input type="text" name="section" class="form-control" value="{{ student.section }}" required>
                </div>
                <button type="submit" class="btn btn-custom">Update</button>
                <a href="/" class="btn btn-secondary mt-2 w-100">Cancel</a>
            </form>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
