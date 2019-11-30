import discord
from discord.ext import commands

import re
import datetime
import sys
import os
import time
import random
import asyncio
import codecs
import io
import requests
import html
import shutil

from decimal import *
from colored import fore, back, style, fg, bg, attr
from pathlib import Path
from math import *
from bs4 import BeautifulSoup

import digiformatter as df

#Version.
version = "0.3.1a"

#Constants.
newline = "\n"
folder = ".."
hdr = {'User-Agent': 'Mozilla/5.0'}

#General commands.
def getID(*names):
    iddict = {}
    with io.open("text/ids.txt", "r", encoding="utf-8") as idfile:
        ids = idfile.readlines()
    ids = [x.strip() for x in ids]
    for line in ids:
        iddict[line[19:]] = line[:18]
    if len(names) == 0:
        return iddict
    if len(names) == 1:
        if names in iddict.keys(): return int(iddict[names])
        else: return 000000000000000000
    else:
        for name in names:
            idlist = []
            for name in names:
                if name in iddict.keys(): idlist.append(int(iddict[name]))
                else: idlist.append(000000000000000000)
            return tuple(idlist)

#Emojify command.
emojidict ={'a': ':regional_indicator_a:',
            'b': ':regional_indicator_b:',
            'c': ':regional_indicator_c:',
            'd': ':regional_indicator_d:',
            'e': ':regional_indicator_e:',
            'f': ':regional_indicator_f:',
            'g': ':regional_indicator_g:',
            'h': ':regional_indicator_h:',
            'i': ':regional_indicator_i:',
            'j': ':regional_indicator_j:',
            'k': ':regional_indicator_k:',
            'l': ':regional_indicator_l:',
            'm': ':regional_indicator_m:',
            'n': ':regional_indicator_n:',
            'o': ':regional_indicator_o:',
            'p': ':regional_indicator_p:',
            'q': ':regional_indicator_q:',
            'r': ':regional_indicator_r:',
            's': ':regional_indicator_s:',
            't': ':regional_indicator_t:',
            'u': ':regional_indicator_u:',
            'v': ':regional_indicator_v:',
            'w': ':regional_indicator_w:',
            'x': ':regional_indicator_x:',
            'y': ':regional_indicator_y:',
            'z': ':regional_indicator_z:',
            'A': ':regional_indicator_a:',
            'B': ':regional_indicator_b:',
            'C': ':regional_indicator_c:',
            'D': ':regional_indicator_d:',
            'E': ':regional_indicator_e:',
            'F': ':regional_indicator_f:',
            'G': ':regional_indicator_g:',
            'H': ':regional_indicator_h:',
            'I': ':regional_indicator_i:',
            'J': ':regional_indicator_j:',
            'K': ':regional_indicator_k:',
            'L': ':regional_indicator_l:',
            'M': ':regional_indicator_m:',
            'N': ':regional_indicator_n:',
            'O': ':regional_indicator_o:',
            'P': ':regional_indicator_p:',
            'Q': ':regional_indicator_q:',
            'R': ':regional_indicator_r:',
            'S': ':regional_indicator_s:',
            'T': ':regional_indicator_t:',
            'U': ':regional_indicator_u:',
            'V': ':regional_indicator_v:',
            'W': ':regional_indicator_w:',
            'X': ':regional_indicator_x:',
            'Y': ':regional_indicator_y:',
            'Z': ':regional_indicator_z:',
            'ａ': ':regional_indicator_a:',
            'ｂ': ':regional_indicator_b:',
            'ｃ': ':regional_indicator_c:',
            'ｄ': ':regional_indicator_d:',
            'ｅ': ':regional_indicator_e:',
            'ｆ': ':regional_indicator_f:',
            'ｇ': ':regional_indicator_g:',
            'ｈ': ':regional_indicator_h:',
            'ｉ': ':regional_indicator_i:',
            'ｊ': ':regional_indicator_j:',
            'ｋ': ':regional_indicator_k:',
            'ｌ': ':regional_indicator_l:',
            'ｍ': ':regional_indicator_m:',
            'ｎ': ':regional_indicator_n:',
            'ｏ': ':regional_indicator_o:',
            'ｐ': ':regional_indicator_p:',
            'ｑ': ':regional_indicator_q:',
            'ｒ': ':regional_indicator_r:',
            'ｓ': ':regional_indicator_s:',
            'ｔ': ':regional_indicator_t:',
            'ｕ': ':regional_indicator_u:',
            'ｖ': ':regional_indicator_v:',
            'ｗ': ':regional_indicator_w:',
            'ｘ': ':regional_indicator_x:',
            'ｙ': ':regional_indicator_y:',
            'ｚ': ':regional_indicator_z:',
            'Ａ': ':regional_indicator_a:',
            'Ｂ': ':regional_indicator_b:',
            'Ｃ': ':regional_indicator_c:',
            'Ｄ': ':regional_indicator_d:',
            'Ｅ': ':regional_indicator_e:',
            'Ｆ': ':regional_indicator_f:',
            'Ｇ': ':regional_indicator_g:',
            'Ｈ': ':regional_indicator_h:',
            'Ｉ': ':regional_indicator_i:',
            'Ｊ': ':regional_indicator_j:',
            'Ｋ': ':regional_indicator_k:',
            'Ｌ': ':regional_indicator_l:',
            'Ｍ': ':regional_indicator_m:',
            'Ｎ': ':regional_indicator_n:',
            'Ｏ': ':regional_indicator_o:',
            'Ｐ': ':regional_indicator_p:',
            'Ｑ': ':regional_indicator_q:',
            'Ｒ': ':regional_indicator_r:',
            'Ｓ': ':regional_indicator_s:',
            'Ｔ': ':regional_indicator_t:',
            'Ｕ': ':regional_indicator_u:',
            'Ｖ': ':regional_indicator_v:',
            'Ｗ': ':regional_indicator_w:',
            'Ｘ': ':regional_indicator_x:',
            'Ｙ': ':regional_indicator_y:',
            'Ｚ': ':regional_indicator_z:',
            '0': ':zero:',
            '1': ':one:',
            '2': ':two:',
            '3': ':three:',
            '4': ':four:',
            '5': ':five:',
            '6': ':six:',
            '7': ':seven:',
            '8': ':eight:',
            '9': ':nine:',
            '０': ':zero:',
            '１': ':one:',
            '２': ':two:',
            '３': ':three:',
            '４': ':four:',
            '５': ':five:',
            '６': ':six:',
            '７': ':seven:',
            '８': ':eight:',
            '９': ':nine:',
            ' ': ' ',
            '!': ':exclamation:',
            '?': ':question:',
            '#': ':hash:',
            '$': ':dollar:',
            '&': ':arrow_forward:',
            '\'': ':arrow_heading_down:',
            '+': ':heavy_plus_sign:',
            '-': ':heavy_minus_sign:',
            '=': ':aquarius:',
            '*': ':asterisk:',
            '.': ':record_button:',
            '^': ':arrow_forward:',
            '>': ':arrow_right:',
            '<': ':arrow_left:',
            '¥': ':yen:',
            '€': ':euro:',
            '£': ':pound:',
            '_': ':heavy_minus_sign:',
            '‽': ':interrobang:',
            ',': ':arrow_up_small:',
            ' ': ' ',
            '！': ':exclamation:',
            '？': ':question:',
            '＃': ':hash:',
            '＄': ':dollar:',
            '＆': ':arrow_forward:',
            '’': ':arrow_heading_down:',
            '‘': ':arrow_heading_down:',
            '＋': ':heavy_plus_sign:',
            '－': ':heavy_minus_sign:',
            '＝': ':aquarius:',
            '＊': ':asterisk:',
            '．': ':record_button:',
            '＾': ':arrow_forward:',
            '＞': ':arrow_right:',
            '＜': ':arrow_left:',
            '￥': ':yen:',
            '＿': ':heavy_minus_sign:',
            newline: newline}

#Wii command.
def getWiiAttribute(soup, attr):
    lookup = soup.find("table", class_="GameData").find("td", string=attr)
    if lookup == None: lookup = soup.find("table", class_="GameData").find("td", string=attr + newline)
    if lookup == None:
        return ""
    returnattr = lookup.next_sibling
    if returnattr == None: return ""

    attrstring = str(returnattr).replace(newline, "")
    if re.search(">(.*?)<", attrstring) != None: return re.search(">(.*?)<", attrstring).group(1)
    return ""

def getWiiAttributes(GAMEID):
    response = requests.get(f"https://www.gametdb.com/Wii/{GAMEID}", headers=hdr)
    soup = BeautifulSoup(response.content, "html.parser")

    attrdict = {}
    attrdict['ID'] = GAMEID
    attrdict['name'] = getWiiAttribute(soup, "title (EN)")
    if attrdict['name'] == "": attrdict['name'] = getWiiAttribute(soup, "title (JP)")
    attrdict['region'] = getWiiAttribute(soup, "region")
    attrdict['type'] = getWiiAttribute(soup, "type")
    attrdict['region'] = getWiiAttribute(soup, "region")
    attrdict['languages'] = getWiiAttribute(soup, "languages")
    attrdict['synopsis'] = getWiiAttribute(soup, "synopsis (EN)")
    if attrdict['synopsis'] == "": attrdict['synopsis'] = getWiiAttribute(soup, "synopsis (JP)")
    attrdict['developer'] = getWiiAttribute(soup, "developer")
    attrdict['publisher'] = getWiiAttribute(soup, "publisher")
    attrdict['date'] = getWiiAttribute(soup, "release date")
    attrdict['genre'] = getWiiAttribute(soup, "genre")
    attrdict['rating'] = getWiiAttribute(soup, "rating")
    attrdict['cover'] = f"https://art.gametdb.com/wii/cover/US/{GAMEID}.png"

    return attrdict

wiidictionary = {}
with io.open("text/wiitdb.txt", encoding="utf-8") as wiidb:
    lines = wiidb.readlines()
    for line in lines:
        splitline = line.split(" = ")
        wiidictionary[splitline[0]] = splitline[1].strip()
