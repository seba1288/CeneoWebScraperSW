from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='Seba'):
    return f"Hello, {name}"