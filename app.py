from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def proxy():
    url = request.args.get('url')
    if url:
        try:
            # Forward the request to the specified URL
            response = requests.get(url)
            response.raise_for_status()
            return jsonify({
                'status': 'success',
                'response': response.text
            })
        except requests.exceptions.RequestException as e:
            return jsonify({
                'status': 'error',
                'message': f"An error occurred: {e}"
            })

    return jsonify({
        'status': 'error',
        'message': 'URL parameter is missing'
    })


