#!/bin/bash


virtenv="$(pip freeze | grep virtualenv)"

if [ $virtenv ]; then
    echo "$virtenv is installed"
else
    echo "need to install virtualenv. Please give your Password for Sudo entry"
    sudo -A pip install virtualenv
fi


virtualenv -p /usr/bin/python2.7 .venv
source .venv/bin/activate
pip install -r PyLoggi/requirements.txt

exit 0
