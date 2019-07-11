from flask_restful import reqparse, Resource, request
from app.controllers import search
from app import app
from flask import render_template, make_response
import json


def search_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('search', type=str, required=True)
    parser.add_argument('force_cache', type=str)
    return parser


class Search(Resource):
    def get(self):
        parser = search_parser()
        data = parser.parse_args()
        query = data['search']
        link = query.replace('https://', '').replace('http://', '')
        if query == "":
            return make_response(render_template('error.html'))
        if search.check_cache(link) == True:
            if data['force_cache'] != 'on':
                print('Serving Cached Package Index for URL:', link)
                template = search.grab_cache(link)
                return make_response(render_template('package.html', template=template))
            else:
                if app.testing == True:
                    print('Serving Un-Cached Package Index for URL:', link)
                pass
        if query == "https://repo.hackyouriphone.org":
            return 500
        if "hackyouriphone" in query.lower():
            return {
                'message': 'Enough. I\'m locking you out.'
            }, 403
        if "discord" in query.lower():
            return {
                'message': 'Go advertise somewhere else cuckold'
            }, 403
        if "twitter" in query.lower():
            return {
                'message': 'Nobody gives a fuck'
            }, 403
        if "castye" in query.lower():
            return {
                'message': 'Fuck off kid'
            }, 403
        if "javascript" in query:
            return {
                'message': 'No XSS'
            }, 403
        if "<script>" in query:
            return {
                'message': 'No XSS'
            }, 403
        while True:
            if query.endswith('/') == True:
                query = query[:-1]
            else:
                break
        search.search_json(query)
        packages = search.get_packages(query)
        list_of = search.packages_to_json(query, packages)
        if list_of == None:
            return make_response(render_template('error.html'))
        template = search.generate_template(list_of)
        search.cache_packages(link, template)
        return make_response(render_template('package.html', template=template))
