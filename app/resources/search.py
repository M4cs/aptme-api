from flask_restful import reqparse, Resource
from app.controllers import search
import json

def search_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('search', type=str, required=True)
    return parser

class Search(Resource):
    def get(self):
        parser = search_parser()
        data = parser.parse_args()
        query = data['search']
        search.search_json(query)
        packages = search.get_packages(query)
        list_of = search.packages_to_json(query, packages)
        return {
            'message': 'komplet',
            # 'packages': packages.decode('utf-8'),
            'cluster_fuck': list_of
        }