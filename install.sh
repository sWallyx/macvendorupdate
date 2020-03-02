#!/bin/bash

create_virtual_env(){
    sudo pip3 install virtualenv
    python3 -m virtualenv env
    source env/bin/activate
    python3 setup.py install
    deactivate
}

not_version_error(){
    echo "You need Python 3 for this application to work";
    echo "Check the FAQ Section in the README for more info.";
    echo " - - - - - - - - - - - - - - - - - - - - - - - -";
    echo "Thanks, bye :)";
}

echo "Making Initial checks:"

# Check if Python 3 is installed
if [[ "$(python3 -V)" =~ "Python 3" ]]; then
    echo "true";
    echo "[OK] -- Python 3 installed"
    create_virtual_env
else
    not_version_error
fi
