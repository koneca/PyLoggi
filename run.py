
import os
os.system('/bin/bash --rcfile shellhelper.sh')

from gevent.wsgi import WSGIServer
from PyLoggi import app

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
