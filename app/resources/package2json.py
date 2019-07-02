from flask_restful import Resource, reqparse
import json
from app.controllers.package2json import packages_to_json, get_packages

def req_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('repo', required=True)
    return parser

class OpenPackage(Resource):
    def get(self):
        parser = req_parser()
        data = parser.parse_args()
        packages = get_packages(data['repo'])
        json_value = packages_to_json(data['repo'], packages)
        return json_value
