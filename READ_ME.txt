python3 -m venv venv
Set-ExecutionPolicy -Scope CurrentUser
Unrestricted
. venv\Scripts\activate
pip install -r requirements.txt
.\app:app.py python -m flask run (doesn't work)
Run app.py code