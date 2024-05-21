from flask import jsonify, request
from config.settings import cursor
from app.models.taxi_model import Taxi
from app.routes.routes import controller_taxis
from psycopg2 import DatabaseError
from app.utils.error_managment import Errors


@controller_taxis.route('', methods=['GET'])
def get_taxis():
    try:
        page = request.args.get('page', 1, type=int) 
        limit = request.args.get('limit', 100, type=int)
        offset = (page - 1) * limit
        cursor.execute("SELECT * FROM taxis ORDER BY id ASC LIMIT %s OFFSET %s", (limit, offset))
        db_taxis = cursor.fetchall()
        if not db_taxis:
            return Errors.handle_404_error(None) #Not found taxis
        taxi_list = [Taxi(db_taxi[0], db_taxi[1]) for db_taxi in db_taxis]
        taxi_dict_list = [taxi.to_dict() for taxi in taxi_list]

        return jsonify(taxi_dict_list)
    except DatabaseError as ex:
        return Errors.handle_500_error(ex)
    except Exception as ex:
        return Errors.handle_500_error(ex)

