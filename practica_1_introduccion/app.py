from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/alumnos')
def alumnos():
    return render_template('alumnos.html')

@app.route('/contactos')
def contacto():
    return render_template('contactos.html')


if __name__ == '__main__':
    app.run(debug=True)