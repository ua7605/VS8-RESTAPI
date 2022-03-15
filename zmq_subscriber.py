import json
import threading
import zmq

import RESTApi
from coordinates_from_vessel import Coordinates
from database import Database
from json_file_loader_reader import write_to_json
from parsing import Parser
from zmq_publisher import Publisher


class Subscriber:
    def __init__(self, ip, port):
        self.subscriber = ZMQSubscriber(ip, port)

    def subscribe(self, topic):
        self.subscriber.subscribe(topic)


class ZMQSubscriber:

    def __init__(self, ip, port):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.bind = 'tcp://' + ip + ':' + port

    def subscribe(self, channel):
        self.socket.connect(self.bind)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, channel)
        worker = threading.Thread(target=self.fetch_updates)
        worker.start()

    def fetch_updates(self):
        # TODO: the IP address needs to be updated to a public one!
        while True:
            message_data = self.socket.recv().decode()
            _, _, message = message_data.partition(":")

            # This is still the old subscriber a newer is available with a callback function.
            # to create a JSON object from the 'message'
            message_in_json_object = json.loads(message)


class ZMQSubscriberSeafar:
    def __init__(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")

        # TODO: uncomment this to run it on the Virtual Wall!
        self.socket.bind("tcp://193.190.127.147:9002")
        # self.socket.bind("tcp://127.0.0.1:9002")
        worker = threading.Thread(target=self.fetch_updates)
        worker.start()

    def fetch_updates(self):
        # TODO: uncomment this to run it on the Virtual Wall!
        publisher = Publisher(ip="193.190.127.147", port="2001")
        # publisher = Publisher(ip="127.0.0.1", port="2001")

        db = Database()

        while True:
            message = self.socket.recv_json()
            # print('Received data of Tercofin II:')
            # print(message)
            # print('\n')

            # TODO: clean this code up, such that it is available in a class or static method. So that here is just
            #  one line

            # This version of the VS8 is already running 24/7 on the server and thus is a stable version.
            # This version is working!!!

            data = Parser(message)

            write_to_json(path='./', file_name='data.json', data=message)

            publisher.publisher_zmq.publish("type", json.dumps({"type": data.type}))

            publisher.publisher_zmq.publish("geometryType", json.dumps({"geometryType": data.geometry_type}))

            publisher.publisher_zmq.publish("latitude", json.dumps({"latitude": data.latitude}))

            publisher.publisher_zmq.publish("longitude", json.dumps({"longitude": data.longitude}))

            publisher.publisher_zmq.publish("sogKph", json.dumps({"sogKph": data.sogKph}))

            publisher.publisher_zmq.publish("headingTrueDegrees",
                                            json.dumps({"headingTrueDegrees": data.headingTrueDegrees}))

            publisher.publisher_zmq.publish("epochSeconds", json.dumps({"epochSeconds": data.epochSeconds}))

            publisher.publisher_zmq.publish("coordinates",
                                            json.dumps(Coordinates(data.latitude, data.longitude).__dict__))

            publisher.publisher_zmq.publish("allData", json.dumps(message))

            # The database is for the moment out commented at the Virtual Wall just for storing puposes sine nobody
            # is using it right now.
            # db.insert(data)
