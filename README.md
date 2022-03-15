# zmqpubsubdemo

Python demo Publisher and Subscriber are using ZMQ. The public IP adress of IMEC server is 193.190.127.147, and port 2001. 
To retrieve data from VS8 you need to make a subscriber (an example is provided in the Python file "subscriber.py"). To retrieve data from a particular topic you give in the name of the topic and a callback funtion to receive and process the data.

## Installation
1. Open a new terminal and download this repository: 
- `git clone https://gitlab.ilabt.imec.be/vcharpentier1/zmqpubsubdemo.git`
2. Install pip3
- `sudo apt-get update`
- `sudo apt-get -y install python3-pip`
3 Install pyzmq
- `sudo pip3 install pyzmq`
4 Install Flask
- `sudo pip3 install flask`
5 Install FlaskRESTful
- `sudo pip3 install Flask-RESTful`

### Run the Publisher
- `cd zmqpubsubdemo`
- `python3 publisher.py`

### Run the Subscriber
- `cd zmqpubsubdemo`
- `python3 subscriber.py`

### How to use the subscriber
1. To retrieve all the data the Seafar vessel sends out you need to subscribe to the topic "allData", like this:
- `subscriber.subscribe(topic="allData", callback=callbackFunc)`
2. Coorinates, to retrieve only the coordinates (longitude, latitude) you need to subscribe to the topic "coordinates", like this:
- `subscriber.subscribe(topic="coordinates", callback=callbackFunc)`
3. longitude, to retrieve only the longitude you need to subscribe to the topic "longitude", like this:
- `subscriber.subscribe(topic="longitude", callback=callbackFunc)`
4. latitude, to retrieve only the latitude you need to subscribe to the topic "latitude", like this:
- `subscriber.subscribe(topic="latitude", callback=callbackFunc)`
5. sogKph, to retrieve only the sogKph you need to subscribe to the topic "sogKph", like this:
- `subscriber.subscribe(topic="sogKph", callback=callbackFunc)`
6. geometryType, to retrieve only the geometryType you need to subscribe to the topic "geometryType", like this:
- `subscriber.subscribe(topic="geometryType", callback=callbackFunc)`
7. headingTrueDegrees, to retrieve only the headingTrueDegrees you need to subscribe to the topic "headingTrueDegrees", like this:
- `subscriber.subscribe(topic="headingTrueDegrees", callback=callbackFunc)`
8. epochSeconds, to retrieve only the headingTrueDegrees you need to subscribe to the topic "epochSeconds", like this:
- `subscriber.subscribe(topic="epochSeconds", callback=callbackFunc)`
9. type, to retrieve only the type you need to subscribe to the topic "type", like this:
- `subscriber.subscribe(topic="type", callback=callbackFunc)`
