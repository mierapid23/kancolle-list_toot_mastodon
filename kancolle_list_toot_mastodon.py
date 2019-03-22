import sys
import os
from mastodon import *

def filecheck(f, text):
	fc = os.path.isfile(f)
	if(fc == False):
		print(text + "ファイルが存在しません")
		sys.exit(1)
	else:
		return

def tootdomain():
	filecheck("api_base_url.txt", "認証")
	api_base_url_text = open("api_base_url.txt", "r")
	api_url = api_base_url_text.read()
	api_base_url_text.close()
	return api_url

def login(domain):
	#認証ファイルチェック
	filecheck("my_clientcred.txt", "認証")
	filecheck("./my_usercred.txt", "認証")

	#ログイン部
	mastodon = Mastodon(
		client_id = "my_clientcred.txt",
		access_token = "my_usercred.txt",
		api_base_url = domain
	)
	return mastodon
	
def main():
	#pathの設定
	os.chdir(os.path.dirname(sys.argv[0]))
	media = sys.argv[1]

	#Tootメディアのチェック
	filecheck(media, "tootする")

	#ログイン
	api_url = tootdomain()
	mastodon = login(api_url)

	#Toot内容の設定
	print(media + " を " + api_url + " にTootします")
	print("Tootするテキストを入力してください")
	toot_text = input()
	while(1):
		print("NSFW/公開範囲/CWの設定をしますか?(Y/N)")
		print("(デフォルト NSFW:False 公開範囲:公開 CW:なし)")
		config = input()
		if(config == "N"):
			image = mastodon.media_post(media)
			mastodon.status_post(toot_text, media_ids = image["id"])
			return 0
		elif(config == "Y"):
			while(1):
				print("NSFWを有効にしますか?(Y/N)")
				nsfw = input()
				if(nsfw == "Y"):
					sensitive = True
					break
				elif(nsfw == "N"):
					sensitive = False
					break
			while(1):
				print("公開範囲を設定してください(1.公開 2.未収載 3.フォロワー限定)")
				input_visibility = input()
				if(input_visibility == "1"):
					visibility = "public"
					break
				elif(input_visibility == "2"):
					visibility = "unlisted"
					break
				elif(input_visibility == "3"):
					visibility = "private"
					break
			while(1):
				print("CWを設定しますか?(Y/N)")
				cw = input()
				if(cw == "Y"):
					print("CWのテキストを入力してください")
					cw_text = input()
					break
				if(cw == "N"):
					cw_text = None
					break
			image = mastodon.media_post(media)
			mastodon.status_post(toot_text, media_ids = image["id"], sensitive = sensitive, visibility = visibility, spoiler_text = cw_text)
			return 0

if __name__ == '__main__':
	#引数チェック
	if(len(sys.argv) != 2):
		print("引数が不正です")
		sys.exit(1)

	main()
