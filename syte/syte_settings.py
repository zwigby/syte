
DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.0'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'zwigby.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'XqZ1CIwOuy9KAi5ULJBQQMCEunkRkvs2ry6zwSzPNWC6Davapo'


#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=true&exclude_replies=true&screen_name='
TWITTER_CONSUMER_KEY = 'K8umnlNtcxZc8hOngCmVbQ'
TWITTER_CONSUMER_SECRET = 'a1nL6TO5u9Lkyivr3ZKY1T9UNX6R46SNVqc95vZvDI'
TWITTER_USER_KEY = '13575682-lmotsvOVgVO2Yt475arZ3Ek6domv60kmUYlL3T6BI'
TWITTER_USER_SECRET = 'eEOpj9odR3icxGaEpqTVrK3WyBAmzpm8rNkPoXS3gQs'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '6e2e65e2dbb50a753ae9e989be5190bd46d9e754'

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = 'eaf51d09989e386e448a'
GITHUB_CLIENT_SECRET = 'efbb7f0c691e6c0a5b7a11ebcccf14457dd4ac74'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = False
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '[ENTER INSTAGRAM ACCESS TOKEN HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_USER_ID = '[ENTER INSTAGRAM USER_ID HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'

INSTAGRAM_OAUTH_ENABLED = False
INSTAGRAM_CLIENT_ID = '[ENTER INSTAGRAM CLIENT_ID HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_CLIENT_SECRET = '[ENTER INSTAGRAM CLIENT_SECRET HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://charliekey.me/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
