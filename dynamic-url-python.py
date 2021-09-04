#!/usr/bin/python
import sys

DYNAMIC_DNS_URL = "https://ipv4.cloudns.net/api/dynamicURL/?q=MzM1MTk3OToyMzkyMTM0MDE6ZjY3MjQ4NmFlYjBjZTE5YTM5YWI3MTYzYjZlN2QxMDk1Yzg4ZmJjOTM1NzA4ZDQxZjExOTViM2ZkMTc4ZTFjYw"
if (sys.version_info[0] < 3):
    import urllib
    page = urllib.urlopen(DYNAMIC_DNS_URL);
    page.close();
else:
    import urllib.request
    page = urllib.request.urlopen(DYNAMIC_DNS_URL);
    page.close();