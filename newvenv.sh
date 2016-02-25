#!/bin/bash

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
python3 -m venv --without-pip "$SCRIPTPATH/venv"
source "$SCRIPTPATH/venv/bin/activate"
curl https://bootstrap.pypa.io/get-pip.py | python
