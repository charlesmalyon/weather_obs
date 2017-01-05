import urllib2
import datetime as datetime

def getCode():
	# index = raw_input("Please type in your index")

	# setting up the time variables
	now = datetime.datetime.now()
	year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute
	starthour = hour -1

	# setting up the url
	url = 'http://www.ogimet.com/display_metars2.php?lang=en&lugar=EGSS+03683&tipo=SA&ord=REV&nil=SI&fmt=txt&ano=%s&mes=%s&day=%s&hora=%s&anof=%s&mesf=%s&dayf=%s&horaf=%s&minf=%s&send=send' % (year,month,day,starthour,year,month,day,hour,minute)

	# taking data from url
	file = []
	for i in urllib2.urlopen(url):
		file.append(i)

	# Search Term
	searchMetar = "METAR"

	# Find the indicies whith the use of searchMetar in.
	indicies = [i for i, s in enumerate(file) if searchMetar in s]

	# The Second in the list(array) will have the one we want.
	fileTemp = file[indicies[1]]

	# Narrow the string down to the right length to input into the other python script
	metarString = fileTemp[13:(len(fileTemp)-2)]

	# Outputs the string we need for the other function.
	return metarString



