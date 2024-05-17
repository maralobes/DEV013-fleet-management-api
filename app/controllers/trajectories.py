from flask import jsonify, request
from config.settings import cursor
from app.models.trajectories_model import Trajectories
from app.routes.routes import controller_trajectories
from datetime import datetime,timedelta


@controller_trajectories.route('/<taxi_id>/<date>', methods=['GET'])
def call_trajectories(taxi_id=0, date=''):
    page = request.args.get('page', 1, type=int) 
    limit = request.args.get('limit', 1, type=int)
    offset = (page - 1) * limit
    print(date)
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    print(date_obj)
    timestamp_str = date_obj.strftime("%Y-%m-%d 00:00:00")
    next_day = date_obj + timedelta(days=1)
    next_day_timestamp = next_day.strftime("%Y-%m-%d 00:00:00")
    print(timestamp_str)
    cursor.execute("SELECT * FROM trajectories WHERE taxi_id = %s AND date >= %s AND date < %s ORDER BY id ASC LIMIT %s OFFSET %s", (taxi_id, timestamp_str, next_day_timestamp, limit, offset))
    db_trajectories = cursor.fetchall()
    print(db_trajectories)
    trajectory_list = [Trajectories(db_trajectory[0], db_trajectory[1], db_trajectory[2], db_trajectory[3], db_trajectory[4]) for db_trajectory in db_trajectories]
    trajectory_dict_list = [trajectory.to_dict() for trajectory in trajectory_list]

    return jsonify(trajectory_dict_list)

@controller_trajectories.route('/latest', methods=['GET'])
def call_last_trajectories():
    page = request.args.get('page', 1, type=int) 
    limit = request.args.get('limit', 1, type=int)
    offset = (page - 1) * limit
    # date_obj = datetime.strptime(date, "%Y-%m-%d")
    # print(date_obj)
    # timestamp_str = date_obj.strftime("%Y-%m-%d 00:00:00")
    # next_day = date_obj + timedelta(days=1)
    # next_day_timestamp = next_day.strftime("%Y-%m-%d 00:00:00")
    # print(timestamp_str)
    cursor.execute("SELECT taxi_id, MAX(date) FROM trajectories GROUP BY taxi_id LIMIT %s OFFSET %s", (limit, offset))
    db_trajectories = cursor.fetchall()
    print(db_trajectories)
    trajectory_list = [Trajectories(db_trajectory[0], db_trajectory[1], db_trajectory[2], db_trajectory[3], db_trajectory[4]) for db_trajectory in db_trajectories]
    trajectory_dict_list = [trajectory.to_dict() for trajectory in trajectory_list]

    return jsonify(trajectory_dict_list)
