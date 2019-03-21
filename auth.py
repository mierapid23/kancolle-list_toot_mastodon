from mastodon import Mastodon

print("インスタンスのドメイン e.g.:kancolle.social")
URL = input()
print("メールアドレス e.g.:example@examle.com")
mail = input()
print("パスワード")
passwd = input()

Mastodon.create_app("kancolle list toot Mastodon", api_base_url = URL , to_file = "my_clientcred.txt")
mastodon = Mastodon(client_id = "my_clientcred.txt", api_base_url = URL)
mastodon.log_in(mail, passwd, to_file = "my_usercred.txt")

f = open("api_base_url.txt", "w")
f.write(URL)
f.close
