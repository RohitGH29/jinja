from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user = {
        "name": "Rohit",
        "age": 28,
        "is_admin": True
    }
    return render_template('index.html', title='User Dashboard', user=user)

if __name__ == '__main__':
    app.run(debug=True)
