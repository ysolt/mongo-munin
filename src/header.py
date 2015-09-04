
import urllib2
import sys
import os  
import pymongo

def getServerStatus():
    if 'MONGO_DB_URI' in os.environ:
      c = pymongo.MongoClient(os.environ['MONGO_DB_URI'])
    else:
      c = pymongo.MongoClient()

    return c.admin.command('serverStatus', workingSet=True)
