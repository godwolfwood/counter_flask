from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "twinjuan"

@app.route('/')
def index():
    if not 'counter' in session:
        session['counter'] = 0
    else:
        process_counter()
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def process_counter():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_counter():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
