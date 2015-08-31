from bottle import route, abort, static_file, HTTPError

@route('/')
@route('/<filename:path>')
def index(filename=''):
    if filename is '': 
        return static_file('/index.html', root='./public')

    file = static_file(filename, root='./public')
    return file