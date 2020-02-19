from dotenv import load_dotenv
import tweepy, os

load_dotenv()

def auth():	
	auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
	auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)		
	
	try:
		api.verify_credentials()	
	except tweepy.TweepError as e:
		print('An error ocurred: ', e.args[0][0]['message'])		

	return api

