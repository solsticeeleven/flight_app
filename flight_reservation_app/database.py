import sqlite3

def connect_db():
    conn = sqlite3.connect('flight_reservations.db')
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

def insert_data(data):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (name, flightNum, destination, date, seatNum)
        VALUES (?, ?, ?, ?, ?)
    ''', (data.name, data.flightNum, data.destination, data.date, data.seatNum))
    conn.commit()
    conn.close()

def fetch_all_reservations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservations')
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_data(data, id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations
        SET name = ?, flightNum = ?, destination = ?, date = ?, seatNum = ?
        WHERE id = ?
    ''', (data.name, data.flightNum, data.destination, data.date, data.seatNum, id))
    conn.commit()
    conn.close()

def delete_data(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reservations WHERE id = ?', (id,))
    conn.commit()
    conn.close()