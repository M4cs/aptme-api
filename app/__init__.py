from flask import Flask, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route('/api')
def index():
    return jsonify({
        'message': 'aptme_api heartbeat endpoint',
        'status': 200
    })

from app.resources.search import Search
api.add_resource(Search, '/api/repos')