#!/usr/bin/python
import sys
DYNAMIC_DNS_URL = "https://ipv4.cloudns.net/api/dynamicURL/?q=MzM1MTk3OToyMzYzMjgzNDI6ZWQwMGM2N2NmYWMyNWE5MzU5ZDI3MGRjODA5OTcwZTk4OTI5YTQwZjhkZWU5YmZiN2IxMWE5OGY0ZjIwMTBmNw"
if sys.version_info[0] < 3:
    import urllib
    page = urllib.urlopen(DYNAMIC_DNS_URL);
    page.close();
else:
    import urllib.request
    page = urllib.request.urlopen(DYNAMIC_DNS_URL);
    page.close();