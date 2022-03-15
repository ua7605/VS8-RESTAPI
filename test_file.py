from database import Database

if __name__ == '__main__':
    database = Database()
    # data = database.db.all()
    # last_row = data[len(data) - 1]
    # print(last_row)
    # print(len(database.db))

    print(database.latest_value())




