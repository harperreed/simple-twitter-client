import oauth2 as oauth
import time
import simplejson

# Set the API endpoint 

class simple_twitter:

    consumer_key = ''
    consumer_secret= ''
    token_key = ''
    token_secret= ''

    def __init__(self, consumer_key, consumer_secret, token_key=None, token_secret=None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        if token_key:
            self.token_key = token_key
        if token_secret:
            self.token_secret = token_secret

        self.consumer = oauth.Consumer(key=self.consumer_key, secret= self.consumer_secret)
        if self.token_key:
            self.token = oauth.Token(key=self.token_key, secret=self.token_secret)
        else:
            self.token = None

        self.client = oauth.Client(self.consumer,self.token)

    def make_request(self, url,method,params=None):
        resp, content = self.client.request(url, method, params)
        self.rate_limit = resp['x-ratelimit-limit']
        self.ratelimit_reset = resp['x-ratelimit-reset']
        content = simplejson.loads(content)
        return content



if __name__ == "__main__": 
    consumer_key=""
    consumer_secret=""
    token_key=""
    token_secret=""

    api = simple_twitter(
            consumer_key=consumer_key, 
            consumer_secret=consumer_secret,
            token_key=token_key, 
            token_secret=token_secret)

    url = "http://api.twitter.com/1/statuses/friends.json"
    print api.make_request(url,"GET")
