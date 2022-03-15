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

    def get_vessel_current_speed(self):
        return self.latest_value()["sogkph"]

    def get_vessel_current_heading(self):
        return self.latest_value()["headingTrueDegrees"]

    def get_vessel_current_location(self):
        return self.latest_value()["latitude"], self.latest_value()["longitude"]

    def get_vessel_historical_data(self):
        return self.db.all()