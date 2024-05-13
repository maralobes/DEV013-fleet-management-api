from flask import jsonify, request
from config.settings import cursor
from app.models.taxi_model import Taxi
from app.routes.routes import controller_taxis


@controller_taxis.route('', methods=['GET'])
def get_taxis():
    page = request.args.get('page', 1, type=int) 
    limit = request.args.get('limit', 100, type=int)
    offset = (page - 1) * limit
    cursor.execute("SELECT * FROM taxis ORDER BY id ASC LIMIT %s OFFSET %s", (limit, offset))
    db_taxis = cursor.fetchall()
    taxi_list = [Taxi(db_taxi[0], db_taxi[1]) for db_taxi in db_taxis]
    # for db_taxi in db_taxis:
    #     taxi_list.append(Taxi(db_taxi[0], db_taxi[1]))
    taxi_dict_list = [taxi.to_dict() for taxi in taxi_list]

    return jsonify(taxi_dict_list)

