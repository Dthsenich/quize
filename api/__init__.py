from flask import Blueprint


api_bp = Blueprint('api', __name__, url_prefix='/api')

from api import authorization_api, leaders_api, tes_process_api

