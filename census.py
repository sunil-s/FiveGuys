import mongodb
from mongodb import *
import csv
import collections


from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()
def sentiments():
         
        #for row in open("/root/src/test/alchemyapi_python/test123.txt","r").readlines():
	#	response = alchemyapi.sentiment("text", row)
	#	print "Sentiment: ", response["docSentiment"]["type"]  
	myText = "I'm excited to get started with AlchemyAPI!"
	response = alchemyapi.sentiment("text", myText)
	print "Sentiment: ", response["docSentiment"]["type"]        
sentiments()         
