from flask import Flask, jsonify

app = Flask(__name__)

# Ruta de ejemplo
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "¡Hola desde el backend!",
        "info": "Este es un ejemplo de API con Flask"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
