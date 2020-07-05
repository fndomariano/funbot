from app_listener import AppListener
from app_subject import AppSubject
from unittest import TestCase

class AppListenerTest(TestCase):

	def test_attach(self):
		observer = AppObserver()
		
		listener = AppListener()
		listener.attach(observer)
		listener.register_messages();
		
		assert len(observer.getChangedUsers()) == 1


