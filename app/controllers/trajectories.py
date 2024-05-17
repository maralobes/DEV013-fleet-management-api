from flask import jsonify, request
from config.settings import cursor
from app.models.trajectories_model import Trajectories
from app.routes.routes import controller_trajectories


@controller_trajectories.route('', methods=['GET'])
def call_trajectories(taxi_id=0):
    page = request.args.get('page', 1, type=int) 
    limit = request.args.get('limit', 1, type=int)
    offset = (page - 1) * limit
    #date = request.args.get('date')
    taxi_id = request.args.get('taxi_id')
    cursor.execute("SELECT * FROM trajectories WHERE taxi_id %s ORDER BY id ASC LIMIT %s OFFSET %s", (taxi_id, limit, offset))
    db_trajectories = cursor.fetchall()
    trajectory_list = [Trajectories(db_trajectory[0], db_trajectory[1], db_trajectory[2], db_trajectory[3], db_trajectory[4]) for db_trajectory in db_trajectories]
    trajectory_dict_list = [trajectory.to_dict() for trajectory in trajectory_list]

    return jsonify(trajectory_dict_list)
