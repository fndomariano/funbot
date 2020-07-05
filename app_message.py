# -*- coding: utf-8 -*-

from app_db import AppMongo
from app_subject import AppSubject

class Message(AppSubject):
	
	content = ''

	def __init__(self, content):
		self.db = AppMongo()
		self.content = content

	def save(self):
		self.db.save(self.content)
		self.notify()

	def is_new(self):
		db = self.db.get_instance()				
		collection = db['messages']
		return collection.count_documents({'message': self.content}) == 0
