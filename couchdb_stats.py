#-*- coding: utf-8 -*-
from requests.auth import HTTPBasicAuth
import requests
from optparse import OptionParser

parser = OptionParser(usage="usage: %prog [-h] [-P PORT] HOSTNAME")
parser.add_option("-H", "--hostname",
                    dest="hostname",
                    action="store",
                    default="127.0.0.1",
                    help="default to localhost")
parser.add_option("-P", "--port",
                    dest="port",
                    action="store",
                    default="5984",
                    help="default port [5984]")
parser.add_option("-u", "--username",
                    dest="username",
                    action="store",
                    default=False,
                    help="Username [optional]")
parser.add_option("-p", "--password",
                    dest="password",
                    action="store",
                    default=False,
                    help="Password [optional]")

(options, args) = parser.parse_args()

# create the url, based on options
if options.username and options.password:
    r = requests.get(str.join('', ('http://', options.hostname,
                    ':', options.port, '/_stats')),
                    auth=HTTPBasicAuth(options.username, options.password))
else:
    r = requests.get(str.join('', ('http://', options.hostname,
                    ':', options.port, '/_stats')))

# check if the response was valid
if r.status_code != 200:
    raise Exception("connection failed!")


def iterator(stats):
    for master, subdict in stats.iteritems():
        print "%s: " % master
        for subkey, subvalue in subdict.iteritems():
            print "    %s: " % subkey
            for value, key in subvalue.iteritems():
                print "       %s: %s" % (value, key)

iterator(r.json())
