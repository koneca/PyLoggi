
import os
import virtualenv
os.system('/bin/bash --rcfile shellhelper.sh')
venv_dir = os.path.join(os.path.expanduser("~"), ".venv")
virtualenv.create_environment(venv_dir)
execfile(os.path.join(venv_dir, "bin", "activate_this.py"))

print ("venv created. Starting.....")

from gevent.pywsgi import WSGIServer
from PyLoggi import create_app

module = create_app(1, 2)

http_server = WSGIServer(('', 8080), module)
http_server.serve_forever()
