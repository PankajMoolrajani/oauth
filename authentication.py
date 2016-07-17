from flask import Blueprint

api_authentication = Blueprint('api_authentication', __name__)

@api_authentication.route('/verify', methods=['GET'])
def verifyCredentials():
    return "success"