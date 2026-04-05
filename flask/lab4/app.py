# app.py
from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/aboutus')
def aboutus():
     return "welcome to about us page \n"   
@app.route('/faq')
def faq():
     return "welcome to FAQ page \n"  
if __name__ == '__main__':
    app.run(debug=True)