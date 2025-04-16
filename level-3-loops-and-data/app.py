from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {"name": "Rohit", "role": "Admin"},
        {"name": "Aisha", "role": "Editor"},
        {"name": "Vikram", "role": "Viewer"},
        {"name": "Nina", "role": "Admin"},
        {"name": "Sofia", "role": "Editor"},
        {"name": "Raj", "role": "Viewer"},
        {"name": "Priya", "role": "Admin"},
        {"name": "Karan", "role": "Editor"},
        {"name": "Anita", "role": "Viewer"},
        {"name": "Sam", "role": "Admin"},
        {"name": "Tina", "role": "Editor"},
        {"name": "Ravi", "role": "Viewer"},
        {"name": "Maya", "role": "Admin"},
        {"name": "Arjun", "role": "Editor"},
        {"name": "Leela", "role": "Viewer"}
    ]
    return render_template('index.html', title="User List", users=users)

if __name__ == '__main__':
    app.run(debug=True)
