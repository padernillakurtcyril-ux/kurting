from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Flask Student API</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(120deg, #4b6cb7, #182848);
                font-family: 'Poppins', sans-serif;
                color: #fff;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                overflow: hidden;
            }
            .card {
                background: rgba(255, 255, 255, 0.95);
                color: #333;
                border-radius: 20px;
                padding: 2.5rem;
                max-width: 500px;
                text-align: center;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
                animation: slideUp 1s ease forwards;
            }
            .card h1 {
                font-weight: 700;
                color: #182848;
                margin-bottom: 0.5rem;
                font-size: 2rem;
            }
            .card p {
                font-size: 1.1rem;
                color: #444;
                margin-bottom: 1.5rem;
            }
            .btn-custom {
                background: linear-gradient(135deg, #4b6cb7, #182848);
                color: white;
                border: none;
                border-radius: 12px;
                padding: 0.8rem 1.8rem;
                font-weight: 600;
                transition: all 0.3s ease;
                text-decoration: none;
                display: inline-block;
            }
            .btn-custom:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 18px rgba(0, 0, 0, 0.3);
                color: #fff;
            }
            footer {
                position: fixed;
                bottom: 10px;
                font-size: 0.9rem;
                color: rgba(255, 255, 255, 0.8);
                text-align: center;
                width: 100%;
            }
            .glow {
                color: #fff;
                text-shadow: 0 0 10px #4b6cb7, 0 0 20px #4b6cb7, 0 0 30px #4b6cb7;
                animation: glowPulse 2s infinite alternate;
            }
            @keyframes slideUp {
                from { opacity: 0; transform: translateY(40px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes glowPulse {
                from { text-shadow: 0 0 10px #4b6cb7, 0 0 20px #4b6cb7; }
                to { text-shadow: 0 0 25px #6f86d6, 0 0 40px #6f86d6; }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1 class="glow">🎓 Flask Student API</h1>
            <p>Welcome! This is your gateway to the <b>Student Information API</b>.</p>
            <a href="/student" class="btn btn-custom">View Student JSON Data</a>
            <hr class="mt-4 mb-3" style="border-color:#ddd;">
            <p style="font-size: 0.95rem; color: #666;">Click the button above to fetch real-time student data in JSON format.</p>
        </div>

        <footer>
            © 2025 Flask Student API • Crafted with 💙 using Bootstrap 5
        </footer>
    </body>
    </html>
    """
    return render_template_string(html)

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
