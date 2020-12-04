import sqlite3


def check_seq_list():
    db = sqlite3.connect(f"Pc_Time.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM Pc_Time")
    count = cursor.fetchone()[0]
    return int(count)


def get_list(sort, desc):
    db = sqlite3.connect(f"Pc_Time.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM Pc_Time")
    count_lists = cursor.fetchone()[0]
    get_list = []
    if int(desc) == 0:
        cursor.execute(f'SELECT * FROM Pc_Time Order By "{sort}"')
    else:
        cursor.execute(f'SELECT * FROM Pc_Time Order By "{sort}" DESC')

    for i in range(count_lists):
        li = cursor.fetchone()[1:]
        get_list.append(li)
    return get_list


def get_recent_data():
    db = sqlite3.connect(f"Pc_Time.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Pc_Time ORDER BY Seq DESC")
    return cursor.fetchone()
