import os
from bottle import route, run
import requests

@route('/')
def pulls():
    r = requests.get("https://api.github.com/repos/openshift/origin/pulls?per_page=3")
    return {'pulls': r.json()}

run(host='0.0.0.0', port=os.getenv('PORT', '8080'), debug=True)
