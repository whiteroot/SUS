class tumblr():

    scheme = 'https'
    url = 'tumblr.com'
    # use a text browser to avoid annoying/blocking javascript
    headers = {'user-agent': 'Lynx/2.8.9dev.16 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/3.5.17'}

    def getHandleUrl(self, handle):
        return "{}://{}.{}".format(tumblr.scheme, handle, tumblr.url)

    def availableHandle(self, r):
        return r.status_code == 404
