# -*- coding: utf-8 -*-

from app_message import Message
from app_observer import AppObserver
from unittest import TestCase

class AppObserverTest(TestCase):

	def test_attach(self):		
		observer = AppObserver()
		message = Message('new content')
		message.attach(observer)		
		assert len(message._observers) == 1


	def test_detach(self):
		observer = AppObserver()
		message = Message('new content 2')
		message.attach(observer)		
		message.detach(observer)				
		assert len(message._observers) == 1
		


