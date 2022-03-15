import json

import requests

from database import Database

if __name__ == '__main__':
    database = Database()
    # data = database.db.all()
    # last_row = data[len(data) - 1]
    # print(last_row)
    # print(len(database.db))

    # print(database.latest_value())
    # print(database.get_vessel_current_speed())
    # print(database.get_vessel_current_heading())
    #print(database.get_vessel_current_location())
    #print(database.get_vessel_historical_data())
    json_string = database.get_vessel_historical_data()#str(database.get_vessel_historical_data()).replace('[', '{', 1).replace(']', '}', 1)
    #print(json_string)
    # print(json_string)
    #normal_obj = json.loads(json_string)
    json_obj = json.dumps(json_string)
    #print(json_obj)




    """
        this is how you need to read the "historicalData" data back in
    """
    print("This is how you need to read back in the data you retrieve from historicalData")
    response = requests.get("http://193.190.127.147:5000/data/historicalData")
    data = response.json()
    json_data = json.loads(data)
    print(json_data[len(json_data) - 1 ])





