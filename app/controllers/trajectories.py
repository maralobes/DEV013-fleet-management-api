from flask import jsonify, request
from config.settings import cursor
from app.models.trajectories_model import Trajectories, LatestTrajectories
from app.routes.routes import controller_trajectories
from datetime import datetime,timedelta
from psycopg2 import DatabaseError, ProgrammingError
from app.utils.error_managment import Errors


def validate_pagination_args(page, limit):
    if page < 1 or limit < 1:
        return False, "Page and limit must be positive integers."
    return True, ""

@controller_trajectories.route('/<taxi_id>/<date>', methods=['GET'])
def call_trajectories(taxi_id=0, date=''):
    try:   
        page = request.args.get('page', 1, type=int) 
        limit = request.args.get('limit', 1, type=int)
        is_valid, error_message = validate_pagination_args(page, limit)
        if not is_valid:
            return Errors.handle_400_error(error_message)
        offset = (page - 1) * limit
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        timestamp_str = date_obj.strftime("%Y-%m-%d 00:00:00")
        next_day = date_obj + timedelta(days=1)
        next_day_timestamp = next_day.strftime("%Y-%m-%d 00:00:00")
        cursor.execute("SELECT * FROM trajectories WHERE taxi_id = %s AND date >= %s AND date < %s ORDER BY taxi_id ASC LIMIT %s OFFSET %s", (taxi_id, timestamp_str, next_day_timestamp, limit, offset))
        db_trajectories = cursor.fetchall()
        if not db_trajectories:
            return Errors.handle_400_error(None) #No trajectories found
        
        trajectory_list = [Trajectories(db_trajectory[0], db_trajectory[1], db_trajectory[2], db_trajectory[3], db_trajectory[4]) for db_trajectory in db_trajectories]
        trajectory_dict_list = [trajectory.to_dict() for trajectory in trajectory_list]

        return jsonify(trajectory_dict_list)
    except ValueError as ex: #Invalid date format
        return Errors.handle_400_error(ex)
    except (DatabaseError, ProgrammingError) as ex:
        return Errors.handle_500_error(ex)
    except Exception as ex:
        return Errors.handle_500_error(ex)

@controller_trajectories.route('/latest', methods=['GET'])
def call_last_trajectories():
    try:
        page = request.args.get('page', 1, type=int) 
        limit = request.args.get('limit', 1, type=int)
        is_valid, error_message = validate_pagination_args(page, limit)
        if not is_valid:
            return Errors.handle_400_error(error_message)
        offset = (page - 1) * limit
        cursor.execute("SELECT DISTINCT ON (t.taxi_id) t.taxi_id, x.plate, t.date, t.latitude, t.longitude FROM (SELECT taxi_id, date, latitude, longitude, ROW_NUMBER() OVER (PARTITION BY taxi_id ORDER BY date DESC) AS row_num FROM trajectories) AS t JOIN taxis x ON t.taxi_id = x.id WHERE t.row_num = 1 LIMIT %s OFFSET %s", (limit, offset))
        db_latest_trajectories = cursor.fetchall()
        if not db_latest_trajectories:
            return Errors.handle_400_error(None) #Not latests trajectories found
        latest_trajectory_list = [LatestTrajectories(db_latest_trajectory[0], db_latest_trajectory[1], db_latest_trajectory[2], db_latest_trajectory[3], db_latest_trajectory[4]) for db_latest_trajectory in db_latest_trajectories]
        latest_trajectory_dict_list = [latest_trajectory.to_dict() for latest_trajectory in latest_trajectory_list]

        return jsonify(latest_trajectory_dict_list)
    except (DatabaseError, ProgrammingError) as ex:
        return Errors.handle_500_error(ex)
    except Exception as ex:
        return Errors.handle_500_error(ex)
