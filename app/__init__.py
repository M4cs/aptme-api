from flask import Flask, jsonify, render_template, send_file
from flask_restful import Api
from app.controllers.rootrender import RootRender

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
    entry = RootRender.generateLeaderboard()
    return render_template('index.html', leaderboard=entry)

@app.route('/assets/css/<css>')
def css(css):
    return send_file('templates/assets/css/{}'.format(css))

@app.route('/assets/js/core/<js>')
def jscore(js):
    return send_file('templates/assets/js/core/{}'.format(js))

@app.route('/assets/js/plugins/<js>')
def jsplugcore(js):
    return send_file('templates/assets/js/plugins/{}'.format(js))

@app.route('/assets/sass/<path>')
def sass(path):
    return send_file('templates/assets/sass/{}'.format(path))

@app.route('/assets/js/<js>')
def js(js):
    return send_file('templates/assets/js/{}'.format(js))

@app.route('/assets/img/<image>')
def image(image):
    return send_file('templates/assets/img/{}'.format(image))

@app.route('/api/assets/css/<css>')
def cssapi(css):
    return send_file('templates/assets/css/{}'.format(css))

@app.route('/api/assets/sass/<path>')
def sassapi(path):
    return send_file('templates/assets/sass/{}'.format(path))

@app.route('/api/assets/js/<js>')
def jsapi(js):
    return send_file('templates/assets/js/{}'.format(js))

@app.route('/api/assets/js/core/<js>')
def jsapicore(js):
    return send_file('templates/assets/js/core/{}'.format(js))

@app.route('/api/assets/js/plugins/<js>')
def jsplugcapiore(js):
    return send_file('templates/assets/js/plugins/{}'.format(js))

@app.route('/api/assets/img/<image>')
def imageapi(image):
    return send_file('templates/assets/img/{}'.format(image))

@app.route('/manifest.json')
def manifest():
    return jsonify({
    "name": "APTMe.io",
    "short_name": "aptme.io",
    "scope": "/",
    "start_url": "/",
    "icons": [
        {
            "src": "./assets/img/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "./assets/img/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        },
        {
            "src": "./assets/img/apple-touch-icon.png",
            "sizes": "512x512",
            "type": "image/png"
        },
        {
            "src": "./assets/img/favicon.ico",
            "sizes": "512x512",
            "type": "image/icon"
        }
    ],
    "theme_color": "#ffee00",
    "background_color": "#0a0a0a",
    "display": "standalone"
})

@app.route('/upup.sw.min.js')
def upup():
    return send_file('app/templates/assets/upup.sw.min.js', mimetype='text/javascript', as_attachment=True, attachment_filename='upup.sw.min.js')

@app.route('/upup.min.js')
def upump():
    return send_file('app/templates/assets/upup.min.js', mimetype='text/javascript', as_attachment=True, attachment_filename='upup.min.js')

@app.route('/apple-touch-icon.png')
def img():
    return send_file('app/templates/assets/img/apple-touch-icon.png', mimetype='image/png')

@app.errorhandler(500)
def fivehundo(self):
    return render_template('error.html')

from app.resources.search import Search
from app.resources.download import Download
from app.resources.package2json import OpenPackage
api.add_resource(Search, '/api/repos')
api.add_resource(Download, '/api/dl')
api.add_resource(OpenPackage, '/api/package2json')