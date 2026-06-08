from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Dockerized Flask Web Application</h1>
    <h2>Created by Jeeva</h2>
    """

@app.route('/about')
def about():
    return "<h2>About Page</h2><p>This application runs inside Docker.</p>"

@app.route('/contact')
def contact():
    return "<h2>Contact Page</h2><p>Email: jeeva@example.com</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)