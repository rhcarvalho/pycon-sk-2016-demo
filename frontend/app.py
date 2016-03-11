import os
from bottle import route, run, view
import requests

PULLS_HOST = os.getenv("PULLS_SERVICE_HOST")
PULLS_PORT = os.getenv("PULLS_SERVICE_PORT")

@route('/')
@view('index')
def pulls():
    if not (PULLS_HOST and PULLS_PORT):
        return {'pulls': []}
    return requests.get("http://{}:{}".format(PULLS_HOST, PULLS_PORT)).json()

run(host='0.0.0.0', port=os.getenv('PORT', '8080'), debug=True)
