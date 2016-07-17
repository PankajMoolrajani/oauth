from flask import Flask
from healthcheck import api_healthcheck

app = Flask(__name__)
app.register_blueprint(api_healthcheck)

@app.route('/')
def oauth():
    return "Monoxor OAuth RESTful Service"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4010)