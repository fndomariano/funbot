# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import tweepy, os

load_dotenv()

def api():		
	auth = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_SECRET_KEY'))
	auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)		
	
	try:
		api.verify_credentials()	
	except tweepy.TweepError as e:
		print('An error ocurred: ', e.args[0][0]['message'])		

	return api