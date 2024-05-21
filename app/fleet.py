from flask import Flask, send_from_directory
from app.controllers.taxi import *
from app.controllers.trajectories import *
from app.routes.routes import *
from flask_swagger_ui import get_swaggerui_blueprint
from app.utils.error_managment import Errors


#Initialize flask app
app = Flask(__name__)

#Register taxis blueprint
app.register_blueprint(controller_taxis, url_prefix='/taxis')

#Register trajectories blueprint
app.register_blueprint(controller_trajectories, url_prefix='/trajectories')

#Create swagger route
@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory('static', path)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Fleet Managment Api"
    }
)
#Register swagger blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

#Register error handling blueprints
app.register_error_handler(400, Errors.handle_400_error)
app.register_error_handler(404, Errors.handle_404_error)
app.register_error_handler(500, Errors.handle_500_error)

if __name__ == '__main__':
    app.run(Debug=True)
