# -*- coding: utf-8 -*-

from app_listener import AppListener

def main():
		
	listener = AppListener()

	print('Searching new messages...')

	while listener.there_is_new_message():
		listener.register_messages()
		

if __name__ == '__main__':
	main()