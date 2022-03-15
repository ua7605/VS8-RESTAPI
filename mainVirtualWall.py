import threading
import time

from RESTApi import app
from zmq_subscriber import ZMQSubscriberSeafar


def start_REST_API():
    # app.run(host="193.190.127.147", debug=True)
    subscriber_seafar = ZMQSubscriberSeafar()
    print("started")


if __name__ == '__main__':
    # This is the main you need to start at the Virtual Wall!!!
    # subscriber_seafar = ZMQSubscriberSeafar()
    thread = threading.Thread(target=start_REST_API)
    thread.start()
    app.run(host="193.190.127.147", debug=True)
