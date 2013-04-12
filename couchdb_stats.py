#-*- coding: utf-8 -*-
from requests.auth import HTTPBasicAuth
import requests
import json

r = requests.get('http://localhost:5984')

# json iterator

def iterator(stats):
    for master, subdict in stats.iteritems():
        print "%s: " % master
        for subkey, subvalue in subdict.iteritems():
            print "    %s: " % subkey
            for value, key in subvalue.iteritems():
                print "       %s: %s" % (value, key)

iterator(r.json())
