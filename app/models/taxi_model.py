class Taxi:
    def __init__(self, id, plate): 
        self.id = id
        self.plate = plate

    def to_dict(self):
        return {
            'id': self.id,
            'plate': self.plate
        }
    