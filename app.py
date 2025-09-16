from flask import flask,render_template
import sqlite3

app = flask (__name__)

def insert_data(nombre,email,telefono,edad,mensaje):
    conn = sqlite3.connect ('database.db')
    c = conn.cursor()
    c.execute ("INSERT INTO contacts (nombre,email,telefono,edad,mensaje) VALUES (?,?,?,?,?))", (nombre,email,telefono,edad,mensaje))
    conn.commit()
    conn.close()
    
@app.router('/contact',methods = ['GET' , 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        edad = request.form['edad']
        mensaje = request.form['telefono']
        
        insert_data(nombre,email,telefono,edad,mensaje)
        
        return 'FORMULARIO ENVIADO CON EXITO'
    return render_template('index.html')