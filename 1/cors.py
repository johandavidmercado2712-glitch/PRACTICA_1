from flask import Flask, jsonify
from flask_cors import CORS # Importamos la extensión

app = Flask(__name__)

# Configuración básica: Permite CORS en todas las rutas para cualquier origen
CORS(app) 

@app.route('/get_tokens', methods=['POST'])
def obtener_tokens():
    # Tu lógica de tokens aquí
    datos = {"token": "abc-123-xyz", "status": "success"}
    
    return jsonify(datos)

# Si usas una Lambda, aquí iría el adaptador (ej. Mangum)
# from mangum import Mangum
# handler = Mangum(app)