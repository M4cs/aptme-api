from flask_restful import Resource, reqparse
from flask import redirect, request
import requests

def download_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('d', required=True)
    parser.add_argument('udid', required=True)
    return parser

class Download(Resource):
    def get(self):
        parser = download_parser()
        data = parser.parse_args()
        dl_link = data['d']
        udid = data['udid']
        headers = {
            'User-Agent': 'Sileo/1 CFNetwork/976 Darwin/18.2.0',
            'X-Firmware': '12.1.2',
            'X-Machine': 'iPhone10,3',
            'X-Unique-ID': udid,
            'Accept': '*/*',
            'Keep-Alive': 'True'
        }
        response = request.Response(headers=headers,
                            is_redirect=True,
                            url=dl_link)
        return response