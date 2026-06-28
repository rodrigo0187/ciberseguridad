from flask import Flask , request
from prometheus_client import start_http_server, Summary

app = Flask(__name__)
REQUEST_TIME= Summary()
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