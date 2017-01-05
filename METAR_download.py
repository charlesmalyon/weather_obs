import urllib2
import datetime as datetime

def getCode(shift):

	# This will be how far back the data goes (In Hours)
	timeShift = shift

	# index = raw_input("Please type in your index")

	# setting up the time variables
	now = datetime.datetime.now()
	year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute
	starthour = (hour - timeShift)

	# setting up the url
	url = 'http://www.ogimet.com/display_metars2.php?lang=en&lugar=EGSS+03683&tipo=SA&ord=REV&nil=SI&fmt=txt&ano=%s&mes=%s&day=%s&hora=%s&anof=%s&mesf=%s&dayf=%s&horaf=%s&minf=%s&send=send' % (year, month, day, starthour, year, month, day, hour, minute)

	# taking data from url
	file = []
	for i in urllib2.urlopen(url):
		file.append(i)

	# Search Term
	searchMetar = "METAR"

	# Find the indicies whith the use of searchMetar in.
	indicies = [i for i, s in enumerate(file) if searchMetar in s]

	# print(indicies)

	dataArray = []


	# Fill an array with the data from the indicies we want.
	for i in indicies:
		dataArray.append(file[i])

	arrayEnd = int(len(dataArray)-2)

	del dataArray[0]

	del dataArray[arrayEnd]

	metarArray = dataArray

	for i in range(0,len(metarArray)):
		tempLen = len(metarArray[i])
		metarArray[i] = metarArray[i][13:tempLen-2]
		# print(metarArray[i])

	# print(metarArray)
	return metarArray

	# The Second in the list(array) will have the one we want.
	# fileTemp = file[indicies[1]]

	# Narrow the string down to the right length to input into the other python script
	# metarString = fileTemp[13:(len(fileTemp)-2)]

	# Outputs the string we need for the other function.
	# return metarString

# getCode(10)



