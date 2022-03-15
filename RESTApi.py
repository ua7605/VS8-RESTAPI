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
api.add_resource(RetrieveVesselData, "/retrieveVesselData")
