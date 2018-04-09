#!/usr/bin/env python

import sys
import json
import urllib2
import base64


def get_from_dict(data_dict, map_list):
    """get the value out of response list"""
    for k in map_list:
        try:
            data_dict = data_dict[k]
        except:
            sys.exit("ERROR: No key " + sys.argv[1])
    return data_dict

if len(sys.argv) < 2:
    print 'please, specify a metric.'
    print ' ex: ./couchdb-stats.py couchdb.httpd.aborted_requests.value'
    sys.exit(1)

try:
    req = urllib2.Request('http://127.0.0.1:5986/_stats')
    stats_json = urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.reason
    exit(1)

METRIC = sys.argv[1].split('.')

RES = get_from_dict(json.load(STATS_JSON), METRIC)
try:
    print int(RES)
except:
    sys.exit('ERROR: Return value cant be converted to int... Value:' + str(RES))
