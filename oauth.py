from flask import Flask
from healthcheck import api_healthcheck
from authentication import api_authentication

app = Flask(__name__)
app.register_blueprint(api_healthcheck)
app.register_blueprint(api_authentication)

@app.route('/')
def oauth():
    return "Monoxor OAuth RESTful Service"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4010)