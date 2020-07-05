# -*- coding: utf-8 -*-

from app_observer import AppObserver

class AppSubject:

	_observers = []

	def attach(self, observer: AppObserver) -> None:
		self._observers.append(observer)

	def detach(self, observer: AppObserver) -> None:
		self._observers.remove(observer)

	def notify(self) -> None:
		for observer in self._observers:
			observer.update(self)