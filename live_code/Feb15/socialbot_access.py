import tweepy 

tokens = []

with open('file.txt', 'r') as f:
  for line in f:
    tokens.append(line.strip())

consumer_key = tokens[0]
consumer_secret = tokens[1]
access_token = tokens[2]
access_token_secret = tokens[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

      statusMessage = "Hi I am an image!"
      api.update_status_with_media(statusMessage,"img/Frame.png")


print("yay")
text = 'yay'
print(".. ", text)