from flask import Flask, request, redirect, render_template, jsonify

app = Flask(__name__)

CORRECT_ANSWER = 7.34

@app.route('/')
def index():
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
            "redirect_url": "/succex"
        })
    else:
        return jsonify({"success": False}), 400

if __name__ == '__main__':
    app.run(debug=True)