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

def reserve(data: dict):
    if data:
        database.insert_data(data)
