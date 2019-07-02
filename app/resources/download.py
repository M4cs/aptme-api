from flask_restful import Resource, reqparse
from flask import redirect
import requests

def download_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('d', required=True)
    parser.add_argument('l', required=True)
    return parser

class Download(Resource):
    def get(self):
        parser = download_parser()
        data = parser.parse_args()
        dl_link = data['d']
        host_link = data['l']
        headers = {
            'User-Agent': 'Sileo/1 CFNetwork/976 Darwin/18.2.0',
            'X-Firmware': '12.1.2',
            'X-Machine': 'iPhone10,3',
            'X-Unique-ID': 'df2b5bc80c02907c03dc65e9f38eedfa350711bb',
            'Authority': host_link,
            'Accept': '*/*',
            'Keep-Alive': 'True'
        }
        response = redirect(dl_link, 200)
        response.headers = headers
        return response