from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# CORRECCION DEFINITIVA: La raiz redirige limpiamente a la ruta del área
@app.route('/')
def inicio():
    return redirect(url_for('area_triangulo'))

# Ruta especifica para calcular el area (esta si maneja GET y POST de forma nativa)
@app.route('/area_triangulo', methods=['GET', 'POST'])
def area_triangulo():
    resultado = None
    if request.method == 'POST':
        try:
            # Obtenemos los datos del formulario HTML
            base = float(request.form.get('base'))
            altura = float(request.form.get('altura'))
            # Aplicamos la formula del area
            resultado = (base * altura) / 2
        except (TypeError, ValueError):
            resultado = "Error en los datos ingresados"

    # Renderiza la plantilla y le pasa la variable 'resultado'
    return render_template('area_triangulo.html', resultado=resultado)

# Rutas adicionales de tu menu de navegacion
@app.route('/suma')
def suma(): 
    return "Pagina de Suma"

@app.route('/resta')
def resta(): 
    return "Pagina de Resta"

@app.route('/multiplicacion')
def multiplicacion(): 
    return "Pagina de Multiplicacian"

@app.route('/division')
def division(): 
    return "Pagina de Division"

@app.route('/perimetro_triangulo')
def perimetro_triangulo(): 
    return render_template('perimetro_triangulo.html')


if __name__ == '__main__':
    app.run(debug=True)
