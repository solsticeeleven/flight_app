import sqlite3

def connect_db():
    conn = sqlite3.connect(r"C:\Users\Maham\Documents\Code\python\flight_reservation_app\flight_reservations.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flightNum TEXT NOT NULL,
            destination TEXT NOT NULL,
            date DATE NOT NULL,
            seatNum TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()



