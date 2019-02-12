#!/usr/bin/env python3

"""
Social Usernames Scraper
Author: Whiteroot
"""
 
import time
import sys
import os
import requests
import random
import logging
import tempfile
from plugins import twitter, instagram, tumblr, pinterest


def usage():
    print ('usage:')
    print ('{} --twitter|--instagram|--tumblr|--pinterest --file <input file>'.format(sys.argv[0]))
    sys.exit(1)

_file = None
socialSitePlugin = None
i = 1
while i < len(sys.argv):
    if sys.argv[i] == '--file':
        _file = sys.argv[i+1]
        i += 2
    elif sys.argv[i] in ('--twitter', '--tw'):
        socialSitePlugin = twitter.twitter()
        i += 1
    elif sys.argv[i] in ('--insta', '--instagram', '--ig'):
        socialSitePlugin = instagram.instagram()
        i += 1
    elif sys.argv[i] in ('--tumblr', '--tr'):
        socialSitePlugin = tumblr.tumblr()
        i += 1
    elif sys.argv[i] in ('--pinterest', '--pt', '--pr', '--ptr'):
        socialSitePlugin = pinterest.pinterest()
        i += 1
    else:
        print ('unknown arg : {}'.format(sys.argv[i]))
        sys.exit(1)
 
if not socialSitePlugin: usage()
if not _file: usage()

_logfilename = os.path.join(tempfile.gettempdir(), "{}.log".format(sys.argv[0]))
logging.basicConfig(format='%(asctime)s [%(filename)s] [%(funcName)s:%(lineno)d] [%(levelname)s] %(message)s', filename=_logfilename, level=logging.INFO, filemode='w')
logging.info('URL: {}'.format(socialSitePlugin.url))

with open(_file) as f:
    for handle in f:
        handle = handle.rstrip()
        url = socialSitePlugin.getHandleUrl(handle)
        try:
            r = requests.get(url, headers=socialSitePlugin.headers)
            logging.info("[{}] status code : {}".format(handle, r.status_code))
            if socialSitePlugin.availableHandle(r):
                print (handle)
        except Exception as e:
            logging.error(e)
            time.sleep(random.randint(112,119))
        time.sleep(random.randint(2,9))
