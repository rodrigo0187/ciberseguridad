from flask import Flask, request
from prometheus_client import generate_latest, start_http_server, Summary, REGISTRY

app = Flask(__name__)

# Línea corregida:
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/hello')
@REQUEST_TIME.time()
def hello():
    name = request.args.get('name', 'Mundo')
    return f"Hello, {name}!"

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)