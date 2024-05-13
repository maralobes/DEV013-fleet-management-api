from flask import jsonify, request
from config.settings import cursor
from app.models.trajectories_model import Trajectories
from app.routes.routes import controller_trajectories


@controller_trajectories.route('', methods=['GET'])
def call_trajectories():
    page = request.args.get('page', 1, type=int) 
    limit = request.args.get('limit', 1, type=int)
    offset = (page - 1) * limit
    # date = request.args.get('date').to_timestamp(date, 'YYY-MM-DD HH24:MI:SS')
    # last_date = (date - 1)
    cursor.execute("SELECT * FROM trajectories WHERE id ORDER BY id ASC LIMIT %s OFFSET %s", (limit, offset))
    records = cursor.fetchall()
    records_list = []
    for record in records:
        records_list.append(Trajectories(record[0], record[1], record[2], record[3], record[4]))

    return jsonify(records_list)
