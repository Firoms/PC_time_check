import sqlite3
import threading
import datetime


class pctime:
    def __init__(self):
        self.check_time_start()

    def check_time_start(self):
        self.start_time = datetime.datetime.now()
        db = sqlite3.connect("Pc_Time.db")
        cursor = db.cursor()
        insert_query = f'INSERT INTO Pc_Time VALUES("","{self.start_time}", "", "")'
        cursor.execute(insert_query)
        db.commit()
        self.update_time()

    def update_time(self):
        self.terminate_time = datetime.datetime.now()
        print(self.terminate_time - self.start_time)
        timer = threading.Timer(1, self.update_time)
        timer.start()


pcstart = pctime()
