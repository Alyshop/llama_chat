from flask import Flask, request, jsonify
from flask_cors import CORS
from llama import run_llama
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    app.logger.debug(f'Received message: {user_input}')
    response = run_llama(user_input)
    app.logger.debug(f'Generated response: {response}')
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
