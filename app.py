from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/appPresident/')
def appPresident():
    return render_template('appPres.html')

@app.route('/customer/')
def customer():
    return render_template('customer.html')

@app.route('/distribution/')
def distribution():
    return render_template('distribution.html')

@app.route('/brewery-management/')
def brewery():
    return render_template('brewery.html')

if __name__ == '__main__':
    app.run(debug=True)
