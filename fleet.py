from config.database import get_connection
from flask import Flask, request, jsonify

app = Flask(__name__)
connection = get_connection()

cursor = connection.cursor()

@app.route('/')
def index():
    return "<p>Hello, World!</p>"

@app.route('/taxis/<id>', methods=['GET'])
def get_taxis():
    taxi_id = request.args.get('id')
    cursor.execute("SELECT * from taxis;")
    record = cursor.fetchall()
    return jsonify(record)
#Close communication with database
#cursor.close()
#connection.close()

@app.route('/trajectories')
def call_trajectories():
    return jsonify(trajectories)

if __name__ == '__main__':
    app.run(debug=True)
