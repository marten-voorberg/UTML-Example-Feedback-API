import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def counter():
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

@app.route('/error/', methods=['POST'])
def always_error():
    return jsonify({
        'status': 'error',
        'errorMessage': 'This always returns an error!'
    })

@app.route('/warning/', methods=['POST'])
def always_warning():
    return jsonify({
        'status': 'warning',
        'errorMessage': 'This always returns a warning!'
    })

@app.route('/diagram/', methods=['POST'])
def always_diagram():
    return jsonify({
        'status': 'success',
        'feedback': {
            'messages': []
        },
        'diagram': {"edges":[],"nodes":[{"type":"CommentNode","width":300,"height":200,"position":{"x":500,"y":100},"text":"This diagram is returned\\nby the API!","hasDoubleBorder":False,"styleObject":{"fill":"white","stroke":"black","stroke-width":2,"fill-opacity":1,"stroke-opacity":0.75}}]}
    })

if __name__ == '__main__':
    app.run()
