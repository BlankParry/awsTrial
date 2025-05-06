# filepath: c:\Users\kmamo\Downloads\ec2trial\pyec2.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homedit():
    return render_template('homedit.html')

@app.route('/newpage', methods=['POST'])
def newpage():
    name = request.form['name']
    return render_template('newpage.html', name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
