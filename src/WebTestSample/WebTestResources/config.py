

def get_url(env):
    if env == 'dev':
        url = 'https://www.google.com'
    elif env == 'qa':
        url = 'https://www.google.com'
    elif env == 'prod':
        url = 'https://www.google.com'
    else:
        print('Environment variable is no recognized')
    return url
