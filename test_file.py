import json

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
    print(json_string)
    # print(json_string)
    #normal_obj = json.loads(json_string)
    json_obj = json.dumps(json_string)
    print(json_obj)
    text:str = "hello"




