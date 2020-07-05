# -*- coding: utf-8 -*-

from app_tweet import api
from app_db import AppMongo
from loguru import logger
import requests, json

class AppListener:

	def __init__(self):
		self.db = AppMongo()
		self.api = api()	

	def register_messages(self):
		db = self.db.get_instance()				
		collection = db['messages']
		
		for item in self.get_messages():			
			message = collection.find({'message': item})

			if message.count() == 0:
				logger.info(item)
				self.db.save(item)
				self.api.update_status(item)
		
	def get_messages(self):
		url = "http://fndomariano.github.io/fun/messages.json"
		response = requests.get(url)	
		data = response.json()
		return data['messages']
