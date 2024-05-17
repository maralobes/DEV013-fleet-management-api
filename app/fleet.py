from flask import Flask, send_from_directory
from app.controllers.taxi import *
from app.controllers.trajectories import *
from app.routes.routes import *
from flask_swagger_ui import get_swaggerui_blueprint


#Initialize flask app
app = Flask(__name__)

#Register taxis blueprint
app.register_blueprint(controller_taxis, url_prefix='/taxis')

#Register trajectories blueprint
app.register_blueprint(controller_trajectories, url_prefix='/trajectories/<taxi_id>')

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

# swagger_template = {
#     "openapi": "3.0.3",  # Update with the version used in your Swagger specification
#     "info": {
#         "title": "Fleet Management API",
#         "description": "The Fleet Management API allows you to request information about taxis.",
#         "version": "1.0.11",
#         "license": {
#             "name": "Apache 2.0",
#             "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
#         }
#     },
#     "servers": [{"url": "http://127.0.0.1:5000"}],  # Update with your server URL
#     "tags": [
#         {"name": "taxis", "description": "Operations about taxis"},
#         {"name": "trajectories", "description": "Operations on trajectories"}
#     ],
#     "components": {
#         "schemas": {
#             # Define your schemas here
#         },
#         "requestBodies": {
#             # Define your request bodies here
#         }
#     }
# }
# swagger = Swagger(app, template=swagger_template, config={
#     'swagger_ui': True,
#     'specs_route': '/apidocs/'
# })

# @app.route('/')
# def index():
#     return "<p>Hello, World!</p>"

# @app.route('/taxis', methods=['GET'])
# def get_taxis():
#     page = request.args.get('page', 1, type=int) 
#     limit = request.args.get('limit', 1, type=int)
#     offset = (page - 1) * limit
#     cursor.execute("SELECT * FROM taxis ORDER BY id ASC LIMIT %s OFFSET %s", (limit, offset))
#     records = cursor.fetchall()
#     records_list = []
#     for record in records:
#         records_list.append({
#             'id' : record[0],
#             'plate' : record[1]
#         })

#     return jsonify(records_list)

# @app.route('/trajectories', methods=['GET'])
# def call_trajectories():
#     page = request.args.get('page', 1, type=int) 
#     limit = request.args.get('limit', 1, type=int)
#     offset = (page - 1) * limit
#     date = request.args.get('date')
#     cursor.execute("SELECT * FROM trajectories WHERE id ORDER BY id ASC LIMIT %s OFFSET %s", (limit, offset))
#     records = cursor.fetchall()
#     records_list = []
#     for record in records:
#         records_list.append({
#             'id' : record[0],
#             'plate' : record[1]
#         })

#     return jsonify(records_list)

if __name__ == '__main__':
    app.run(debug=True)
