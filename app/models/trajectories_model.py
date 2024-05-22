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
    
class LatestTrajectories:
    def __init__(self, taxi_id, plate, date, latitude, longitude):
        self.taxi_id = taxi_id
        self.plate = plate
        self.date = date
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):
        return {
            'taxi_id': self.taxi_id,
            'plate': self.plate,
            'date' : self.date,
            'latitude': self.latitude,
            'longitude': self.longitude
        }