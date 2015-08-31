from bottle import request, abort, route
from ..storage.helpers import create_throwaway

@route(method='POST')
def emgen():
    if not request.json:
        return abort(400, 'You must pass a valid json object')

    if not request.json['email']:
        return abort(400, 'Must pass a valid email')
        
    id = create_throwaway(email=request.json['email'])

    if not id is False:
        return {
            "data": {
                "email": "%s@emgen.io" % str(id),
            }
        }