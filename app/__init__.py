from flask import Flask, jsonify, render_template, send_file
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route('/api')
def index():
    return jsonify({
        'message': 'aptme_api heartbeat endpoint',
        'status': 200
    })

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/assets/css/<css>')
def css(css):
    return send_file('templates/assets/css/{}'.format(css))

@app.route('/assets/sass/<path>')
def sass(path):
    return send_file('templates/assets/sass/{}'.format(path))

@app.route('/assets/js/<js>')
def js(js):
    return send_file('templates/assets/js/{}'.format(js))

@app.route('/assets/images/<image>')
def image(image):
    return send_file('templates/assets/images/{}'.format(image))

@app.route('/api/assets/css/<css>')
def cssapi(css):
    return send_file('templates/assets/css/{}'.format(css))

@app.route('/api/assets/sass/<path>')
def sassapi(path):
    return send_file('templates/assets/sass/{}'.format(path))

@app.route('/api/assets/js/<js>')
def jsapi(js):
    return send_file('templates/assets/js/{}'.format(js))

@app.route('/api/assets/images/<image>')
def imageapi(image):
    return send_file('templates/assets/images/{}'.format(image))

@app.errorhandler(500)
def fivehundo():
    return render_template('error.html')

from app.resources.search import Search
from app.resources.download import Download
api.add_resource(Search, '/api/repos')
api.add_resource(Download, '/api/dl')