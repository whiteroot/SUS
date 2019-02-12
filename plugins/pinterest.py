class pinterest():

    scheme = 'https'
    url = 'pinterest.com'
    headers = {'user-agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)'}

    def getHandleUrl(self, handle):
        return "{}://{}/{}".format(pinterest.scheme, pinterest.url, handle)

    def availableHandle(self, r):
        return '"location": {"pathname": "/?show_error=true",' in r.text or r.status_code == 404
