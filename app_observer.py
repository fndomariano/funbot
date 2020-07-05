# -*- coding: utf-8 -*-

from app_tweet import api
from loguru import logger 

class AppObserver:
	
	def update(self, subject) -> None:		
		logger.info(subject.content)			
		api().update_status(subject.content)