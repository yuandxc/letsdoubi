import tweepy

consumer_key = 'duXvAgTq4VdLcL2iEi539krNQ'
consumer_secret = 'FjZlUXWqeIDLIa02oAgdRZuln6ErQtY1cRWNcZZfkstbdjBTh0'
access_token = '1025683382-AqdI8Wm115vQXhhXz02Lrpg9Xrh9hxAguRryaLX'
access_token_secret = '3jmSNxSCtUmEJ8VmWRRY9iCuOCFze35Epu48L8ssxDNcv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#wsj_tweets = api.search(q='Kelsi Hoser',count=100)
#wsj_tweets = api.search(q='gtx 1080',rpp=100)
for status in tweepy.Cursor(api.search,
                            q='Alteryx',
                            include_entities=True,
                            lang="en").items(3):
    print(status.text)
    print(status.created_at)
    print(status.id_str)

#for tweet in wsj_tweets:
#    print('***************')
#    print(tweet.created_at)
 #   print(tweet.text)
#    print(tweet.user.followers_count)
#    print(tweet.is_quote_status)
   # print(tweet.reply_count)
 #   print(tweet.favorited)
