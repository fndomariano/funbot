# -*- coding: utf-8 -*-

from app_tweet import api
from app_db import AppMongo
import requests, json

class AppListener:

	def __init__(self):
		self.db = AppMongo()
		self.api = api()

	def there_is_new_message(self):
		site_messages = self.get_messages()
		db = self.db.get_instance()
		collection = db['messages']
		
		if (len(site_messages) > collection.count()):
			return True						
		return False

	def register_messages(self):
		print('Registering messages')
		for message in self.get_messages():
			self.db.save(message)
			# self.api.update_status(message)
		
	def get_messages(self):
		url = "http://fndomariano.github.io/fun/messages.json"
		response = requests.get(url)	
		data = response.json()
		return data['messages']
