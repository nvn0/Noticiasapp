from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Endpoint para buscar dados de notícias
@app.route('/noticias', methods=['GET'])
def get_noticias():
    try:
        # URL da API externa que contém os dados
        url = 'http://4.180.0.81/noticias'
        
        # Fazendo a requisição GET para a API externa
        response = requests.get(url)
        
        # Verifica se a resposta foi bem-sucedida (status code 200)
        if response.status_code == 200:
            # Retorna os dados como JSON
            return jsonify(response.json())
        else:
            # Se a resposta não for bem-sucedida, retorna uma mensagem de erro
            return jsonify({'error': f'Failed to fetch data from {url}', 'status_code': response.status_code}), response.status_code
    
    except Exception as e:
        # Se ocorrer algum erro durante a requisição, retorna uma mensagem de erro
        return jsonify({'error': str(e)}), 500


@app.route('/triste', methods=['GET'])
def get_noticias_tristes():
    try:
        # URL da API externa que contém os dados
        url = 'http://4.180.0.81/triste'
        
        # Fazendo a requisição GET para a API externa
        response = requests.get(url)
        
        # Verifica se a resposta foi bem-sucedida (status code 200)
        if response.status_code == 200:
            # Retorna os dados como JSON
            return jsonify(response.json())
        else:
            # Se a resposta não for bem-sucedida, retorna uma mensagem de erro
            return jsonify({'error': f'Failed to fetch data from {url}', 'status_code': response.status_code}), response.status_code
    
    except Exception as e:
        # Se ocorrer algum erro durante a requisição, retorna uma mensagem de erro
        return jsonify({'error': str(e)}), 500


# Roda o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
