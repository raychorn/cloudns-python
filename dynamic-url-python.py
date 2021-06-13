#!/usr/bin/python

import sys
import json

import time

__cache__ = {}
 
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

while (1):
    req = Request("http://httpbin.org/ip")
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        print('Reason: ', e.reason)
    else:
        data = json.loads(response.read())
        _origin = data.get("origin")
        assert isinstance(_origin, str) and (len(_origin) > 0), 'Something went wrong. Please fix.'
        print("The public IP is : %s" % _origin)
        __cache__[_origin] = __cache__.get('ip', 0) + 1
        num_found = len(list(__cache__.keys()))
        detections = [(v > 2) for v in list(__cache__.values())]
        test1 = (num_found > 1)
        test2 = all(detections)
        prediction = (test1) and (test2)
        print('DEBUG: Number of IPs found: {} ({}) --> {} ({}) -> [{}]'.format(num_found, test1, detections, test2, prediction))
        if (prediction):
            print('The ip address has changed.')
            DYNAMIC_DNS_URL = "https://ipv4.cloudns.net/api/dynamicURL/?q=MzM1MTk3OToyMzYzMjgzNDI6ZWQwMGM2N2NmYWMyNWE5MzU5ZDI3MGRjODA5OTcwZTk4OTI5YTQwZjhkZWU5YmZiN2IxMWE5OGY0ZjIwMTBmNw"
            if sys.version_info[0] < 3:
                import urllib
                page = urllib.urlopen(DYNAMIC_DNS_URL);
                page.close();
            else:
                import urllib.request
                page = urllib.request.urlopen(DYNAMIC_DNS_URL);
                page.close();    
            __cache__ = {}
        print('Completed one check.')
        time.sleep(10)
