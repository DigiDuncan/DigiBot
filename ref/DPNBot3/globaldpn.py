import discord
from discord.ext import commands
import re
import datetime
import sys
import os
import time
from datetime import date
from datetime import *
import math
import random
from decimal import *
from colored import fore, back, style, fg, bg, attr
from pathlib import Path
import string
import traceback
from discord.ext import commands
from math import *
import asyncio
import codecs

#TODO: Make this do something useful.
class DigiException(Exception):
	pass

#Version.
version = "2.0.1"

#Constants
newline = "\n"
monikalines = ["What? I don't know anyone named Monika.",
"I don't know anyone named Monika! hehheh...",
"Hey wha-- er...", "Did someone say my n- um... Monika? Weird.",
"I hear Monika was the best character in Doki Doki. I may be a bit biased though 'cause... never mind.",
"Monika? :sweat_smile: Never heard of her."]
folder = ".."
digiid = 271803699095928832

#Monika line gen.
def monikaline():
	return random.choice(monikalines)

def regenhexcode():
	#16-char hex string gen for unregister.
	hexdigits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
	lst = [random.choice(hexdigits) for n in range(16)]
	hexstring = "".join(lst)
	hexfile = open("hexstring.txt", "r+")
	hexfile.write(hexstring)
	hexfile.close()

def readhexcode():
	#Read the hexcode from the file.
	hexfile = open("hexstring.txt", "r+")
	hexcode = hexfile.readlines()
	hexfile.close()
	return str(hexcode[0])

#ASCII art.
ascii = """
          ((%&
          *********(#&
         (*****************/(&
         ****************************(#&
        (************************************/(&&
        ***///////////*************////////////********((###           ####
       (***/############/*********/((((((((((((((/******/((((***(&     ((((
       ****(##(//////(####/*******/(((/******//((((*****/((((/********/((((
      (***/###/********/###/******((((*********/(((/***/((((((/*******/(((*****
      ****/###**********(###/*****(((/*********/(((/***/(((/(((/******(((/*****
     (****(##(**********/###/****/(((*********/(((/****(((/*/(((/****/(((/****
     ****/###/**********/###/****/(((///////(((((/*****(((/**/(((/***/(((****/
    (****/##(/**********(###/***/((((((((((((((/******/(((****/(((/**/((/****
    *****(##(**********/###(****/(((******************/((/*****/(((//(((/***/
    ****/###/*********/###(*****(((/*****************/(((/******/(((/((/****
   (****/##(********/####/*****/(((/*****************/((/********((((((/***/
   *****(##((((((######(*******/(((******************(((/********/(((((****
  /****/###########(//*********(((/*****************/(((/*********/(((/****
  *************************************************************************
  *****/##################################################/***************
       #((((((((((((((((((((((((((((((((((((((((((((((((((((((((/********/
       #((((((((((((((((((((((((((((((((((((((((((((((((((((((((///////**
       /(((((((((((((((((((((((((//////////////////////////////////////*/
                                     ***********************************
                                              */***********************/
                                                       ****************
                                                                */****/
																"""

#Tasks
tasks = {}
