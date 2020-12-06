from checkpctime import pctime
import sqlite3


# class TestClass:
#     def test_pctime_init(self):
#         self.db = sqlite3.connect(
#             "C:/코딩/컴퓨터_사용시간_프로그램/Pc_Time.db", check_same_thread=False
#         )
#         self.cursor = self.db.cursor()
#         assert str(self.db)[1:19] == "sqlite3.Connection"
#         assert str(self.cursor)[1:15] == "sqlite3.Cursor"

#     def test_read_row_num(self):
#         num = pctime.read_row_num(self)
#         assert type(num) == int
