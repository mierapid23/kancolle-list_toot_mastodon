from mastodon import Mastodon

print("Instance URL e.g.:https://kancolle.social")
URL = input()
print("mail address e.g.:example@examle.com")
mail = input()
print("password")
passwd = input()

Mastodon.create_app("kancolle list toot Mastodon", api_base_url = URL , to_file = "my_clientcred.txt")
mastodon = Mastodon(client_id = "my_clientcred.txt", api_base_url = URL)
mastodon.log_in(mail, passwd, to_file = "my_usercred.txt")

f = open("api_base_url.txt", "w")
f.write(URL)
f.close
