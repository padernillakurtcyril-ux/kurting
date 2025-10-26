from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# --- Home Route ---
@app.route('/')
def home():
    html = """
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
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: #ffffff;
                color: #333;
                border: none;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
                padding: 2rem;
                max-width: 450px;
                text-align: center;
                animation: fadeIn 1s ease;
            }
            .card h1 {
                font-size: 1.8rem;
                color: #182848;
                font-weight: 700;
            }
            .btn-custom {
                background-color: #4b6cb7;
                color: white;
                border-radius: 10px;
                border: none;
                padding: 0.7rem 1.5rem;
                transition: 0.3s;
            }
            .btn-custom:hover {
                background-color: #3551a2;
            }
            footer {
                position: absolute;
                bottom: 15px;
                font-size: 14px;
                color: rgba(255,255,255,0.7);
            }
            @keyframes fadeIn {
                from {opacity: 0; transform: translateY(10px);}
                to {opacity: 1; transform: translateY(0);}
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🎓 Welcome to My Flask API!</h1>
            <p class="mt-3">Explore the <b>Student API</b> endpoint below.</p>
            <a href="/student" class="btn btn-custom mt-2">View Student Info (JSON)</a>
        </div>
        <footer>© 2025 Flask API Demo | Beautiful by Bootstrap 💙</footer>
    </body>
    </html>
    """
    return render_template_string(html)

# --- API Endpoint ---
@app.route('/student')
def get_student():
    student_data = {
        "name": "Juan Dela Cruz",
        "grade": 10,
        "section": "Zechariah"
    }
    return jsonify(student_data)

if __name__ == '__main__':
    app.run(debug=True)
