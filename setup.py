#!/bin/bash

pip install virtualenv
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
pip install -r PyLoggi/requirements.txt

exit 0
