from index import *
from flask import render_template, request

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Descripcion')
def descripcion():
    return render_template('Descripcion.html')    

#loging
@app.route('/Login')
def Login():
    return render_template('Login.html')

#agregar contacto
@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
       fullname = request.form['fullname']
       phone = request.form['phone']
       email = request.form['email']
       direction = request.form['direction']
       dni = request.form['dni']
       password = request.form['password']
       cur = mysql.connection.cursor()
       #cur.(SELECT *FROM flaskcontacts)
       cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
       mysql.connection.commit()
       return render_template('home.html')