import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def hello_world():
    data = request.get_json()

    if data is None:
        return jsonify({
            'status': 'error',
            'errorMessage': 'The request does not have a body!'
        })

    if 'diagram' not in data:
        return jsonify({
            'status': 'error',
            'errorMessage': 'The request body does not contain a diagram!'
        })

    diagram = data['diagram']

    return jsonify({
        'status': 'success',
        'feedback': {
            'messages': [
                {
                    'type': 'success',
                    'message': f'Your diagram contains {len(diagram["nodes"])} nodes.'
                },
                {
                    'type': 'warning',
                    'message': f'Your diagram contains {len(diagram["edges"])} edges.'
                },
            ]
        }
    })


if __name__ == '__main__':
    app.run()
