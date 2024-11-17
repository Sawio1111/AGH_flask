#!/bin/bash

if [ "$1" == "dev" ]; then
    echo "Uruchamianie w trybie developerskim"
    export FLASK_ENV=development
    export FLASK_APP=app.py
    flask run
else
    echo "Uruchamianie w trybie produkcyjnym"
    export FLASK_ENV=production
    export FLASK_APP=app.py
    flask run --host=0.0.0.0 --port=5000
fi
