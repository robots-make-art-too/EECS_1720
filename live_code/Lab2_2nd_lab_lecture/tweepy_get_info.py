#==============================================================
# Import any libraries to use |  
# TWEEPY is the python API library to connect twitter
#==============================================================
import tweepy
#==============================================================
# WE HAVE DONE THIS LAST FEW LECTURES/CODE | NOT NEW
# you can add the tokens you generate to a "file.txt"
# one per line - then just access them using this snippet
#==============================================================
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

API = tweepy.API(auth)

#==============================================================
#==============================================================
# NEW CONTENT: Here is a list of some info we can grab from
# an account; we will use __CodeBot__ for the example 
# 
# GUESS WHAT? We are doing OOP and JSON without even knowing it
#==============================================================
#==============================================================

# the screen name of the user
screen_name = "__CodeBot__"

# fetching the user
user = API.get_user(screen_name=screen_name)

#==============================================================
# Here we print to the screen
# To save to a file uncomment the with open line below
# indent all the print statements
# replace print(" with file.write("\n
# to return printing to screen, re-comment out the with open
# then un-indent all file.write statments
# then replace file.write("\n with print("
#==============================================================
# 
with open('out.txt', 'w+') as file:
	file.write("OUTPUT of tweepy_get_info\n#==============================================================\n")
#
# you can find the JSON data dictionary here:
# https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
# 
#==============================================================
# CONNECTION TO OOP? 
#==============================================================
# a Tweet is an `Object`
# is has root-level `Attributes` (i.e., id, created_at)
# Tweet `Objects` are the `parent` `Class`
# with `children` (i.e., user, place (if geo-tagged))
#==============================================================
#
# printing the information
#
#==============================================================
# JSON OBJECTS
#==============================================================
# Here we are handling JSON data as accessed from twitter
# these are a mix of `Attributes` and `child` `Objects`
#
	file.write("\nThe id is : " + str(user.id))
	file.write("\nThe id_str is : " + user.id_str)
	file.write("\nThe name is : " + user.name)
	file.write("\nThe screen_name is : " + user.screen_name)
	file.write("\nThe location is : " + str(user.location))
	file.write("\nThe profile_location is : " + str(user.profile_location))
	file.write("\nThe description is : " + user.description)


	file.write("\nThe url is : " + user.url)
	file.write("\nThe entities are : " + str(user.entities))
	file.write("\nIs the account protected? : " + str(user.protected))


	file.write("\nThe followers_count is : " + str(user.followers_count))
	file.write("\nThe friends_count is : " + str(user.friends_count))
	file.write("\nThe listed_count is : " + str(user.listed_count))
	file.write("\nThe account was created on : " + str(user.created_at))
	file.write("\nThe favourites_count is : " + str(user.favourites_count))
	file.write("\nThe utc_offset is : " + str(user.utc_offset))
	file.write("\nThe geo_enabled is : " + str(user.geo_enabled))
	file.write("\nThe verified is : " + str(user.verified))
	file.write("\nThe statuses_count is : " + str(user.statuses_count))
	file.write("\nThe lang is : " + str(user.lang))
	file.write("\nThe status ID is : " + str(user.status.id))
	file.write("\nThe contributors_enabled is : " + str(user.contributors_enabled))
	file.write("\nThe is_translator is : " + str(user.is_translator))
	file.write("\nThe is_translation_enabled is : " + str(user.is_translation_enabled))


	file.write("\nThe profile_background_color is : " + user.profile_background_color)
	# file.write("\nThe profile_background_image_url is : " + user.profile_background_image_url)
	# file.write("\nThe profile_background_image_url_https is : " + user.profile_background_image_url_https)
	file.write("\nThe profile_background_tile is : " + str(user.profile_background_tile))
	file.write("\nThe profile_image_url is : " + user.profile_image_url)
	file.write("\nThe profile_image_url_https is : " + user.profile_image_url_https)
	# file.write("\nThe profile_banner_url is : " + user.profile_banner_url)
	file.write("\nThe profile_link_color is : " + user.profile_link_color)
	file.write("\nThe profile_sidebar_border_color is : " + user.profile_sidebar_border_color)
	file.write("\nThe profile_sidebar_fill_color is : " + user.profile_sidebar_fill_color)
	file.write("\nThe profile_text_color is : " + user.profile_text_color)
	file.write("\nThe profile_use_background_image is : " + str(user.profile_use_background_image))


	file.write("\nThe has_extended_profile is : " + str(user.has_extended_profile))
	file.write("\nThe default_profile is : " + str(user.default_profile))
	file.write("\nThe default_profile_image is : " + str(user.default_profile_image))
	file.write("\nIs the authenticated user following the account? : " + str(user.following))


	file.write("\nHas the authenticated user requested to follow the account? : " + str(user.follow_request_sent))
	file.write("\nAre notifications of the authenticated user turned on for the account? : " + str(user.notifications))

#==============================================================
#==============================================================
#
# ERRORS TO LOOK OUT FOR:
#
#==============================================================
#==============================================================
# above, I have commented out 3 lines - these return errors
# when the script is run | this is because __CodeBot__ doesn't
# have these features installed AND our code does not
# handle the errors 
#
# The errors codes diplayed when the script fails are
# two TypeErrors and one AttributeError
#==============================================================
#==============================================================
#
# print("The profile_background_image_url is : " + user.profile_background_image_url)
#
# Traceback (most recent call last):
#   File "tweepy_get_info.py", line 83, in <module>
#     print("The profile_background_image_url is : " + user.profile_background_image_url)
# TypeError: can only concatenate str (not "NoneType") to str
#
#==============================================================
#
# print("The profile_background_image_url_https is : " + user.profile_background_image_url_https)
#
# Traceback (most recent call last):
#   File "tweepy_get_info.py", line 84, in <module>
#     print("The profile_background_image_url_https is : " + user.profile_background_image_url_https)
# TypeError: can only concatenate str (not "NoneType") to str
#
#==============================================================
#
# print("The profile_banner_url is : " + user.profile_banner_url)
#
# Traceback (most recent call last):
#   File "tweepy_get_info.py", line 88, in <module>
#     print("The profile_banner_url is : " + user.profile_banner_url)
# AttributeError: 'User' object has no attribute 'profile_banner_url'
#
#==============================================================
#==============================================================
#
# Final errors you might encounter if you try to access an
# incorrect screen_name
#
#==============================================================
#
# Traceback (most recent call last):
#   File "tweepy_get_info.py", line 41, in <module>
#     user = API.get_user(screen_name=screen_name)
#   File "/home/unknown/.local/lib/python3.8/site-packages/tweepy/api.py", line 46, in wrapper
#     return method(*args, **kwargs)
#   File "/home/unknown/.local/lib/python3.8/site-packages/tweepy/api.py", line 2426, in get_user
#     return self.request(
#   File "/home/unknown/.local/lib/python3.8/site-packages/tweepy/api.py", line 261, in request
#     raise NotFound(resp)
# tweepy.errors.NotFound: 404 Not Found
# 50 - User not found.
#
#==============================================================
# Notice these are nearly the same error except in the case 
# above, the user is not found, screen_name = __CodB__ 
# and in the case below the user is suspended or it is a 
# blocked name format, screen_name = _CodeBot
#==============================================================
#
#     return self.request(
#   File "/home/unknown/.local/lib/python3.8/site-packages/tweepy/api.py", line 259, in request
#     raise Forbidden(resp)
# tweepy.errors.Forbidden: 403 Forbidden
# 63 - User has been suspended.

