from config.database import get_connection
from flask import Flask, request, jsonify

app = Flask(__name__)
connection = get_connection()

cursor = connection.cursor()


@app.route('/')
def index():
    return "<p>Hello, World!</p>"

@app.route('/taxis', methods=['GET'])
def get_taxis():
    page = request.args.get('page', 1, type=int) 
    limit = request.args.get('limit', 1, type=int)
    offset = (page - 1) * limit
    cursor.execute("SELECT * FROM taxis ORDER BY id ASC LIMIT %s OFFSET %s", (limit, offset))
    records = cursor.fetchall()
    records_list = []
    for record in records:
        records_list.append({
            'id' : record[0],
            'plate' : record[1]
        })

    return jsonify(records_list)

@app.route('/trajectories')
def call_trajectories():
    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)
