from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/ip/<ip>')
def consultar_ip(ip):
    try:
        resposta = requests.get(f"http://ip-api.com/json/{ip}")
        dados = resposta.json()
        
        if dados.get("status") == "fail":
            return jsonify({"erro": "IP inválido"}), 400
        
        return jsonify({
            "ip": dados.get("query"),
            "pais": dados.get("country"),
            "cidade": dados.get("city"),
            "provedor": dados.get("isp"),
            "latitude": dados.get("lat"),
            "longitude": dados.get("lon")
        })
    except:
        return jsonify({"erro": "Erro ao consultar o IP"}), 500

if __name__ == '__main__':
    app.run(debug=True)
