import datetime
import json
import csv
import urllib2
# The counties New York City are:

# 005 - Bronx
# 047 - Kings (Brooklyn)
# 061 - New York (Manhattan)
# 081 - Queens
# 085 - Richmond (Staten Island)
if __name__ == '__main__':
  url = "http://api.nytimes.com/svc/semantic/v2/geocodes/query.json?name=NYC&api-key=c25da189dc898bad942beacfd7a78565:13:74782268"	
  request = urllib2.urlopen(url)
  metadata = json.loads(request.read())
  
  print metadata
  try:
	  for i in range(len(metadata['results'][0])):
	  	print metadata['results'][i]['name']
  except:
  	  pass	  	



