import database

def fetch_all_reservations():
    conn = database.connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservations')
    rows = cursor.fetchall()
    conn.close()
    return rows