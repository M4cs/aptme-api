from flask_restful import Resource
import json

class TopRepos(Resource):
    def get(self):
        with open('app/db/link_count.json', 'r+') as json_file:
            data = json.load(json_file)
            sortdict = [(k, data[k]) for k in sorted(data, key=data.get, reverse=True)]
        return sortdict