from flask import Flask
from app.controllers.taxi import *
from app.controllers.trajectories import *
from app.routes.routes import *
from flasgger import Swagger



app = Flask(__name__)
app.register_blueprint(controller_taxis, url_prefix='/taxis')
app.register_blueprint(controller_trajectories, url_prefix='/trajectories')
endpoints_documentation = Swagger(app)

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
