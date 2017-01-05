from metar import Metar
from METAR_download import getCode

code = getCode()

obs = Metar.Metar(code)

print("temperature: %s" % obs.temp.string("C"))

