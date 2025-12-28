from flask import Flask, request, redirect, session, render_template, jsonify

app = Flask(__name__)
app.secret_key = 'hellokitty'

CORRECT_ANSWER = 7.34

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route('/')
def hello():
    if not session.get('started'):
        return render_template('hello.html')
    else:
        return render_template('404.html'), 404

@app.route('/cmon')
def cmon():
    if not session.get('started'):
        return render_template('cmon.html')
    else:
        return render_template('404.html'), 404

@app.route('/final')
def final():
    if not session.get('started'):
        return render_template('final.html')
    else:
        return render_template('404.html'), 404

@app.route('/index')
def index():
    session['started'] = True
    return render_template('index.html')

@app.route('/rickroll')
def rickroll():
    return render_template('rickroll.html')

@app.route('/run-button')
def run_button():
    return render_template('run-button.html')

@app.route('/simpson')
def simpson():
    return render_template('simpson.html')

@app.route('/speedor')
def speedor():
    return render_template('speedor.html')

@app.route('/succex')
def succex():
    return render_template('succex.html')

@app.route('/verify-answer', methods=['POST'])
def verify_answer():
    data = request.json
    user_val = data.get('answer')

    if user_val and abs(user_val - CORRECT_ANSWER) < 0.01:
        return jsonify({
            "success": True, 
            "redirect_url": "/speedor"
        })
    else:
        return jsonify({"success": False}), 400

if __name__ == '__main__':
    app.run(debug=True)
