from flask import jsonify, request
from config.settings import cursor
from app.models.taxi_model import Taxi
from app.routes.routes import controller_taxis


@controller_taxis.route('', methods=['GET'])
def get_taxis():
    """Get list of taxis and pagination
    ---
    parameters:
      - name: query
        in: query
        description: Plate
        required: false
        schema:
          type: string
      - name: page
        in: query
        description: Page
        required: false
        schema:
          type: integer
          default: 1
      - name: limit
        in: query
        description: Number of elements per page
        required: false
        schema:
          type: integer
          default: 10
    responses:
      '200':
        description: successful operation
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    format: int64
                    example: 974
                  plate:
                    type: string
                    example: "FNDF-2678"
            examples:
              AllUsers:
                value:
                  - id: 974
                    plate: "HIJ-876"
                  - id: 8974
                    plate: "UTRW-8967"
                  - id: 2345
                    plate: "PFD-9954"
    """
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

