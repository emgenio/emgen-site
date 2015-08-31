from bottle import run, default_app
from . import *

app = default_app()

def main ():
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)