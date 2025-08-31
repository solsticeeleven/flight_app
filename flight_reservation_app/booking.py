import database

class Data:
    def __init__(self, name, flightNum, destination, date, seatNum):
        self.name = name
        self.flightNum = flightNum
        self.destination = destination
        self.date = date
        self.seatNum = seatNum

    def update_data(self, name=None, flightNum=None, destination=None, date=None, seatNum=None):
        if name:
            self.name = name
        if flightNum:
            self.flightNum = flightNum
        if destination:
            self.destination = destination
        if date:
            self.date = date
        if seatNum:
            self.seatNum = seatNum

def insert_data(data):
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (name, flightNum, destination, date, seatNum)
        VALUES (?, ?, ?, ?, ?)
    ''', (data.name, data.flightNum, data.destination, data.date, data.seatNum))
    conn.commit()
    conn.close()

def reserve(data: dict):
    if data:
        insert_data(data)
