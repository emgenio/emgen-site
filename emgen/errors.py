from bottle import error, response

@error(501)
def error501(error):
    from simplejson import dumps
    response.set_header('Content-Type', 'application/json')
    return dumps({
        'errors':[
            {'status':'Endpoint not yet implemented', 'code':'501', 'reason':error.body}
        ],
        'data':None
    })

@error(400)
def error400(error):
    from simplejson import dumps
    response.set_header('Content-Type', 'application/json')
    return dumps({
        'errors':[
            {'status':'Bad Request', 'code':'400', 'reason':error.body}
        ],
        'data':None
    })

@error(403)
def error403(error):
    from simplejson import dumps
    response.set_header('Content-Type', 'application/json')
    return dumps({
        'errors':[
            {'status':'Access Not Allowed', 'code':'403', 'reason':error.body}
        ],
        'data':None
    })

@error(404)
def error404(error):
    from simplejson import dumps
    response.set_header('Content-Type', 'application/json')
    return dumps({
        'errors':[
            {'status':'No endpoint at this location', 'code':'404'}
        ],
        'data':None
    })

@error(405)
def error405(error):
    from simplejson import dumps
    response.set_header('Content-Type', 'application/json')
    return dumps({
        'errors':[
            {'status':'Method Not Allowed', 'code':'405', 'reason':error.body}
        ],
        'data':None
    })