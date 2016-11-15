import sys


if hasattr(sys, 'real_prefix'):
    print "aber hallo"

print (".venv created. Starting.....")

from gevent.pywsgi import WSGIServer
from PyLoggi import create_app

module = create_app(1, 2)

http_server = WSGIServer(('', 5000), module)
http_server.serve_forever()
