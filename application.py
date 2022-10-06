from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Sup'


application.run(host='0.0.0.0', debug=True, port=5000)