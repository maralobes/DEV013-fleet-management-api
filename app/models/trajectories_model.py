class Trajectories:
    def __init__(self, id, plate, date, latitude, longitude):
        self.id = id
        self.plate = plate
        self.date = date
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):
        return {
            'id': self.id,
            'plate': self.plate,
            'date' : self.date,
            'latitude': self.latitude,
            'longitude': self.longitude
        }
    