
import os
import virtualenv

venv_dir = os.path.join(os.getcwd(), ".venv")
print "Using virtual env: ",venv_dir

venv_path = os.path.join(venv_dir, "bin", "activate")
print "starting virtual env: ",venv_path

os.system('/bin/bash --rcfile shellhelper.sh')

print (".venv created. Starting.....")

from gevent.pywsgi import WSGIServer
from PyLoggi import create_app

module = create_app(1, 2)

http_server = WSGIServer(('', 5000), module)
http_server.serve_forever()
