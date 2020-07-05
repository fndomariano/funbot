# -*- coding: utf-8 -*-

from app_message import Message
from app_observer import AppObserver
from loguru import logger
import requests, json

class AppListener:

	def register_messages(self) -> None:		
		observer = AppObserver()
		for content in self._get_messages():
			message = Message(content)
			if (message.is_new()):
				message.attach(observer)
				message.save()

	def _get_messages(self) -> []:
		url = "http://fndomariano.github.io/fun/messages.json"
		response = requests.get(url)	
		data = response.json()		
		return data['messages']
		