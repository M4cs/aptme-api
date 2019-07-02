from flask_restful import reqparse, Resource
from app.controllers import search
from flask import render_template, make_response
import json

def search_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('search', type=str, required=True)
    return parser

class Search(Resource):
    def get(self):
        try:
            parser = search_parser()
            data = parser.parse_args()
            query = data['search']
            if "hackyouriphone" in query:
                return {
                    'message': 'Enough. I\'m locking you out.'
                }, 403
            if query.endswith('/') == True:
                query = query[:-1]
            search.search_json(query)
            packages = search.get_packages(query)
            list_of = search.packages_to_json(query, packages)
            template = search.generate_template(list_of)
            return make_response(render_template('package.html', template=template))
        except:
            return make_response(render_template('error.html'))