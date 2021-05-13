import sqlite3
import os


class TableAlreadyExist(Exception):pass

class DatabaseSQL:
	def __init__(self,database_name,database_path=os.getcwd()):
		self.database_name = database_name
		self.database_path = database_path
		self.con = sqlite3.connect(f"{self.database_path}\\{self.database_name}")
		self.cur = self.con.cursor()
	
	def create_table(self,table_name,columns):
		try:
			self.cur.execute(f"CREATE TABLE {table_name} {columns}")
		except:
			raise TableAlreadyExist(f"'{table_name} table already in {self.database_name}.")
	
	def add_values(self,table_name,*values):
		for value in values:
			self.cur.execute(f"INSERT INTO {table_name} VALUES {value}")
			self.con.commit()
	
	def get_values(self,value_to_get,table_name,**values):
		pass		