from flask_restful import reqparse, Resource, request
from app.controllers import search
from flask import render_template, make_response
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
        if search.check_cache(query) == True:
            list_of = search.grab_cache(query)
            template = search.generate_template(list_of)
            return make_response(render_template('package.html', template=template))
        if query == "https://repo.hackyouriphone.org":
            print(request.remote_addr)
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
        if "nepeta" in query:
            return {
                'message': 'Nep has been blacklisted. Blame Castyte for abusing it'
            }, 403
        if "javascript" in query:
            return {
                'message': 'No XSS'
            }, 403
        if "<script>" in query:
            return {
                'message': 'No XSS'
            }, 403
        if query.endswith('/') == True:
            query = query[:-1]
        search.search_json(query)
        packages = search.get_packages(query)
        list_of = search.packages_to_json(query, packages)
        search.cache_packages(query, list_of)
        template = search.generate_template(list_of)
        return make_response(render_template('package.html', template=template))
