
### Setup

Requirements: Python 3, Flask

To run: 

- Setup a virtual env, install dependencies
```
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

- Run flask app
```
FLASK_APP=botrank.py flask run
```

This should spawn the web app on port 5000 of localhost.

### Production setup

To run this app in production, you'll need to run a server that supports
WSGI applications to handle concurrency.

You can use gunicorn, a popular pre-forked multiprocess WSGI HTTP server.

To run your app through gunicorn (with 4 worker processes on port 5000):

```
gunicorn -w 4 -b 127.0.0.1:5000 botrank:app
```