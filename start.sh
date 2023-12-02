# for linux
#export FLASK_APP=app.py; export PYTHONPATH=.; export FLASK_DEBUG=1;
#flask run --host=0.0.0.0

# for windows
$env:FLASK_APP = "app.py"
$env:PYTHONPATH = "."
$env:FLASK_DEBUG = "1"
flask run --host=0.0.0.0