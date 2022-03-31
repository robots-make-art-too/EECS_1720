import json

# maybe a json format works for you

data = {
	"keys": [
		{
			"consumer_key": "",
			"consumer_secret": "",
			"access_token": "",
			"access_token_secret": ""
		}
	]	
}

with open("tokens_file.json", "w") as write:
	json.dump(data, write)
