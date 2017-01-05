from metar import Metar
from METAR_download import getCode

import plotlyLogin

import plotly.plotly as py
import plotly.graph_objs as go

login = plotlyLogin.username
api = plotlyLogin.api

py.sign_in(login, api)

# You can put in the brakets how far back you want to go (in hours)

codes = getCode(10)

# print(codes)

obs = []

# Fills the array 'obs' with METAR objects
for i in range(0, len(codes)):
	obs.append(Metar.Metar(codes[i]))

# From this you can call any object in the array and ask for its METAR properties
# Print is just an example of this

# print(obs[4].temp)

# Arrays to hold all of this specific data.
tempTimes = []  # This is a really awkward datetime.datetime object
tempWindSpeeds = []  # This doesn't help because its still in METAR format
tempTemps = []  # Also in an annoying METAR format

for i in range(0, len(codes)):
	tempTimes.append(obs[i].time)
	tempWindSpeeds.append(obs[i].wind_speed)
	tempTemps.append(obs[i].temp)

dates = []  #Bit of an afterthought but easier to see when it was in output

times = []
temps = []
winds = []


# If you want the raw text with "C" and "knots" use the 'temp' arrays before I have adjusted them.

# This was a right ball ache
# I had to convert back and forth in order to concatonate it right
# This only deals with the 'times' array
for i in range(0, len(codes)):
	times.append(int((str(tempTimes[i].hour)) + str(tempTimes[i].minute)))
	dates.append(int((str(tempTimes[i].month) + str(tempTimes[i].day))))

# The 'temps' needed to be converted to a string in order to put them into
# an array. God knows why. There must be an easier way to do that.
for i in range(0, len(codes)):
	temps.append(str(tempTemps[i]))
	temps[i] = temps[i][0:-2]  #Removes the 'C' at the end

# Same again for 'windspeed'. This could bite me later.
for i in range(0, len(codes)):
	winds.append(str(tempWindSpeeds[i]))
	winds[i] = winds[i][0:-6]

trace0 = go.Scatter(
	x = times,
	y = temps,
	mode = 'lines',
	name = 'Temperatures (In C)'
)

trace1 = go.Scatter(
	x = times,
	y = winds,
	mode = 'lines',
	name = 'Wind Speed (In Knots)'
)

data = [trace0, trace1]

py.plot(data, filename = 'test')