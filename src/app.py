from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def base():
    return render_template('calculator.html')


@app.route('/logs')
def logs():
    return render_template('logs.html')

    
if(__name__=='__main__'):
    app.run(debug=True)