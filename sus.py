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
from platform import system

HEADER = {'user-agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)'}


def usage():
    print ('usage:')
    print ('{} --twitter|--instagram --file <input file> [--debug]'.format(sys.argv[0]))
    sys.exit(1)

_debug = False
_file = ''
_socialSiteUrl = None
i = 1
while i < len(sys.argv):
    if sys.argv[i] == '--file':
        _file = sys.argv[i+1]
        i += 2
    elif sys.argv[i] in ('--twitter', '--tw'):
        _socialSiteUrl = 'https://twitter.com'
        i += 1
    elif sys.argv[i] in ('--insta', '--instagram', '--ig'):
        _socialSiteUrl = 'https://instagram.com'
        i += 1
    else:
        print ('unknown arg : {}'.format(sys.argv[i]))
        sys.exit(1)
 
if not _socialSiteUrl: usage()
if not _file: usage()

_logfilename = os.path.join(tempfile.gettempdir(), "{}.log".format(sys.argv[0]))
logging.basicConfig(format='%(asctime)s [%(filename)s] [%(funcName)s:%(lineno)d] [%(levelname)s] %(message)s', filename=_logfilename, level=logging.INFO, filemode='w')
logging.info('URL: {}'.format(_socialSiteUrl))

with open(_file) as f:
    for twittos in f:
        twittos = twittos.rstrip()
        url = _socialSiteUrl + '/' + twittos
        try:
            r = requests.get(url, headers=HEADER)
            logging.info("[{}] status code : {}".format(twittos, r.status_code))
            if r.status_code == 404:
                print (twittos)
        except:
            t = random.randint(112,119)
            time.sleep(t)
        t = random.randint(2,9)
        time.sleep(t)
