# -*- coding: utf-8 -*-

from app_listener import AppListener

def main():
	listener = AppListener()

	print('Searching new messages...')

	while True:
		listener.register_messages()
		

if __name__ == '__main__':
	main()