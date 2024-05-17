class Trajectories:
    def __init__(self, id, taxi_id, date, latitude, longitude):
        self.id = id
        self.taxi_id = taxi_id
        self.date = date
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):
        return {
            'id': self.id,
            'taxi_id': self.taxi_id,
            'date' : self.date,
            'latitude': self.latitude,
            'longitude': self.longitude
        }
    