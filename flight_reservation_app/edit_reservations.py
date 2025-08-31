import database

def update_data(data, id):
    if not id:
        id = data[0]
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations
        SET name = ?, flightNum = ?, destination = ?, date = ?, seatNum = ?
        WHERE id = ?
    ''', (data.name, data.flightNum, data.destination, data.date, data.seatNum, id))
    conn.commit()
    conn.close()

def delete_data(id):
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reservations WHERE id = ?', (id,))
    conn.commit()
    conn.close()