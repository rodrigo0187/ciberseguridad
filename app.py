from flask import Flask , request

app = Flask(__name__)

@app.route('/hello')
def hello():
    """Endpoint para saludar al usuario
    
    Parámetros:
    name(str): Nombre del usuario

    Returns:
        str: Mensaje de saludo.
    """    
    name= request.args.get('name')
    return f'hello {name}'

if __name__ == "main":
    app.run(debug=True)