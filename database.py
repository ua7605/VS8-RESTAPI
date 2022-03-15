from tinydb import TinyDB, Query
from parsing import Parser


class Database:
    def __init__(self):
        self.db = TinyDB("db.json")

    def insert(self, data: Parser):
        self.db.insert({
            'type': data.type,
            'geometry': data.geometry_type,
            'latitude': data.latitude,
            'longitude': data.longitude,
            'sogkph': data.sogKph,
            'headingTrueDegrees': data.headingTrueDegrees,
            'epochSeconds': data.epochSeconds
        })

    def latest_value(self):
        data = self.db.all()
        return data[len(data) - 1]
