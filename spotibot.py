import spotipy
import config


class SpotiBot:
	def __init__(self):
		self.scope = 'user-library-read playlist-read-private'
		self.uri = 'http://localhost:9090'
		self.token = None
		self.authorize()

	def authorize(self, username=config.username, client_id=config.client_id, client_secret=config.client_secret):
		self.token = spotipy.prompt_for_user_token(username=username, scope=self.scope, client_id=client_id,
		                                           client_secret=client_secret, redirect_uri=self.uri)

	def get_saved_tracks(self):
		if self.token:
			spotibot = spotipy.Spotify(auth=self.token)
			results = spotibot.current_user_saved_tracks(limit=50)
			for item in results['items']:
				track = item['track']
				print(track['name'] + ' - ' + track['artists'][0]['name'])
		else:
			print("Can't get token!")


SpotiBot().authorize()
SpotiBot().get_saved_tracks()