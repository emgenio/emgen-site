from bottle import request, abort, route
from ..storage.helpers import create_throwaway
import re

@route(method='POST')
def emgen():
    if not request.json:
        return abort(400, 'You must pass a valid json object')

    if not request.json['email']:
        return abort(400, 'Must pass a valid email')
        
    if not re.match(r"[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", request.json['email']):
        return abort(400, 'Must pass a valid email')

    if request.json['email'].find('@emgen.io'):
        return abort(400, 'Must pass a valid email. Not an emgen one you sneaky severus snape.')



    id = create_throwaway(email=request.json['email'])

    if not id is False:
        return {
            "data": {
                "email": "%s@emgen.io" % str(id),
            }
        }