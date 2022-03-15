import json

from flask import Flask, request
from flask_restful import Api, Resource

from database import Database
from json_file_loader_reader import read_json_file

app = Flask(__name__)
api = Api(app)
database = Database()


class RetrieveVesselData(Resource):
    def get(self):
        return database.latest_value()
        # return read_json_file(file_name="data.json")


class VesselSpeed(Resource):
    def get(self):
        return {"speed": database.get_vessel_current_speed()}


class VesselHeading(Resource):
    def get(self):
        return {"heading": database.get_vessel_current_heading()}


class VesselLocation(Resource):
    def get(self):
        location = database.get_vessel_current_location()
        return {"latitude": location[0], "longitude": location[1]}


class VesselHistoricalData(Resource):
    def get(self):
        return str(database.get_vessel_historical_data()).replace('[', '{', 1).replace(']', '}', 1)


class HelloWorld(Resource):
    def get(self):
        return {"about": "Hello world"}

    def post(self):
        some_json = request.get_json()
        return {"you sent": some_json}, 201


class Multi(Resource):
    def get(self, num):
        return {"result": num * 10}


api.add_resource(HelloWorld, "/helloworld")
api.add_resource(Multi, "/multi/go/<int:num>")
api.add_resource(RetrieveVesselData, "/data")
api.add_resource(VesselSpeed, "/data/speed")
api.add_resource(VesselHeading, "/data/heading")
api.add_resource(VesselLocation, "/data/location")
api.add_resource(VesselHistoricalData, "/data/historicalData")
