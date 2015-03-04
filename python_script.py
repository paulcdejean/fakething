#!/usr/bin/python
import os

#import boto
#from boto.s3.connection import S3Connection
#from boto.s3.key import Key

#print "Hello boto"

result = {
    "project": "twb-firmware",
    "branch": "",
    "commit": "",
    "urls": []
    }

result["project"] = os.environ["CI_PROJECT"]
result["branch"] = os.environ["CI_BRANCH"]
result["commit"] = os.environ["CI_COMMIT_ID"]

print "This doesn't work"
