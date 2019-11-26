import discord
from discord.ext import commands
from globalWIP import *
import requests
import random
import os

os.system("")
print(load("convert.py loaded." + style.RESET))

def toSV(value, unit):
    if unit.lower() in ["meter", "meters", "metre", "metres", "m"]:
        return value
    elif unit.lower() in ["centimeter", "centimeters", "centimetre", "centimetres" "cm"]:
        return value / (10**2)
    elif unit.lower() in ["millimeter", "millimeters", "millimetre", "millimetres", "mm"]:
        return value / (10**3)
    elif unit.lower() in ["micrometer", "micrometers", "micrometre", "micrometres", "um"]:
        return value / (10**6)
    elif unit.lower() in ["nanometer", "nanometers", "nanometre", "nanometres", "nm"]:
        return value / (10**9)
    elif unit.lower() in ["kilometer", "kilometers", "kilometre", "kilometres", "km"]:
        return value * (10**3)
    elif unit.lower() in ["megameter", "megameters", "megametre", "megametres"]:
        return value * (10**6)
    elif unit.lower() in ["gigameter", "gigameters", "gigametre", "gigametres", "gm"]:
        return value * (10**9)
    elif unit.lower() in ["terameter", "terameters", "terametre", "terametres", "tm"]:
        return value * (10**12)
    elif unit.lower() in ["petameter", "petameters", "petametre", "petametres", "pm"]:
        return value * (10**15)
    elif unit.lower() in ["exameter", "exameters", "exametre", "exametres", "em"]:
        return value * (10**18)
    elif unit.lower() in ["zettameter", "zettameters", "zettametre", "zettametres", "zm"]:
        return value * (10**21)
    elif unit.lower() in ["yottameter", "yottameters", "yottametre", "yottametres", "ym"]:
        return value * (10**24)
    elif unit.lower() in ["inch", "inches"]:
        return value / 39.3
    elif unit.lower() in ["foot", "feet"]:
        return value / 3.281
    elif unit.lower() in ["yard", "yards"]:
        return value / 1.094
    elif unit.lower() in ["lightyears", "lightyear", "ly"]:
        return value * 9.461 * (10**15)
    elif unit.lower() in ["earth", "earths"]:
        return value * 14792020
    elif unit.lower() in ["sun", "suns"]:
        return value * 1.391 * (10**9)
    elif unit.lower() in ["pc", "parsecs", "parsec"]:
        return value * 3.086 * (10**16)
    else:
        return -1

print(str(toSV(49, "km")) + " meters")
os.system("pause")
