# -*- coding: utf-8 -*-

from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

class AppMongo:

	def __init__(self):
		self.client = MongoClient("mongodb://%s:%s" %(os.getenv('DB_HOST'), os.getenv('DB_PORT')))

	def get_instance(self):		
		db_name = os.getenv('DB_NAME')		
		return self.client[db_name]		
		
	def save(self, message):
		try:
			db = self.get_instance()
			collection = db['messages']
			collection.insert_one(message)
		except Exception as e:
			print('An error ocurred: ', str(e))	
	
		



	