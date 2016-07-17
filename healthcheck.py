from flask import Blueprint

api_healthcheck = Blueprint('api_healthcheck', __name__)

@api_healthcheck.route('/health', methods=['GET'])
def getHealthcheck():
    return "HealthCheck: OK"