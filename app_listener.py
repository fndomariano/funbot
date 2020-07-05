# -*- coding: utf-8 -*-

from app_tweet import api
from app_db import AppMongo
from app_subject import AppSubject
from loguru import logger
import requests, json

class AppListener(AppSubject):

	def __init__(self):
		self.db = AppMongo()
		self.api = api()	

	def update(self):

		self.notify()

		if message.count() == 0:
			logger.info(item)
			# self.db.save(item)
			# self.api.update_status(item)
		
	def _get_messages(self):
		url = "http://fndomariano.github.io/fun/messages.json"
		response = requests.get(url)	
		data = response.json()
		return data['messages']

	def _has_new_messages(self):
		db = self.db.get_instance()				
		collection = db['messages']		

		for item in self._get_messages():			
			message = collection.find({'message': item})