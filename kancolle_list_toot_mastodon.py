import sys
from mastodon import *

api_base_url_text = open("api_base_url.txt", "r")
api_url = api_base_url_text.read()
api_base_url_text.close()
mastodon = Mastodon(
	client_id = "my_clientcred.txt",
	access_token = "my_usercred.txt",
	api_base_url = api_url
)

print("add " + sys.argv[1] + " to toot to " + api_url)
print("input toot text")
toot_text = input()

image = mastodon.media_post(sys.argv[1])
	
mastodon.status_post(toot_text, media_ids = image["id"])
