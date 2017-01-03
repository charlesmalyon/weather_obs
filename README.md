# weather_obs

You need to install the package from the following:

https://github.com/tomp/python-metar 

This package allows you to decode a METAR code (a METAR is a weather report at a given site, usually an airport). Each site has a 4 letter name, e.g. London City Airport is EGLC. A respository of names can be found on: 

http://weather.rap.ucar.edu/surface/stations.txt

You just need to find your station name and then use the get_report script to get your decoded report. The test that compliments this 'metar_decoded.py' is attempting to take this report in preparation for plotting.

CMal 03/01/2017 
