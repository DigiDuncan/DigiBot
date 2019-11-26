import discord
from discord.ext import commands
import os
import random
from decimal import *
from colored import fore, back, style, fg, bg, attr
from time import strftime, localtime

def load(message):
	return (fg(238) + message + style.RESET)

os.system("")
print(load("globalWIP.py loaded." + style.RESET))

#Constants
botname = "WIPBot"
version = "b.0.4.1"
prefix = '$'
newline = "\n"
monikalines = ["What? I don't know anyone named Monika.",
"I don't know anyone named Monika! hehheh...",
"Hey wha-- er...", "Did someone say my n- um... Monika? Weird.",
"I hear Monika was the best character in Doki Doki. I may be a bit biased though 'cause... never mind.",
"Monika? :sweat_smile: Never heard of her."]
bot_id = 489713545882370049
digi_id = 271803699095928832

#Emojis
emojiBlank = '<:blank:495790900434173952>'
emojiGreenGem = '<:gg:495817625700532225>'
emojiYellowGem = '<:yg:495817627965325313>'
emojiRedGem = '<:rg:495817626027687938>'
emojiBlueGem = '<:bg:495817626564558849>'
emojiOrangeGem = '<:og:495817626090733568>'
emojiOpen1 = '<:open1:495817626220757002>'
emojiOpen2 = '<:open2:495817626086408192>'
emojiOpen3 = '<:open3:495817625855721513>'
emojiOpen4 = '<:open4:495817625998196747>'
emojiOpen5 = '<:open5:495817626187202560>'
emojiGreenTap = '<:gt:496028633442287626>'
emojiYellowTap = '<:yt:496028633543213060>'
emojiRedTap = '<:rt:496028633635356683>'
emojiBlueTap = '<:bt:496028633396150283>'
emojiOrangeTap = '<:ot:496028633425510401>'
emojiGreenHOPO = '<:gh:496028633408995368>'
emojiYellowHOPO = '<:yh:496028633404801025>'
emojiRedHOPO = '<:rh:496028633257869362>'
emojiBlueHOPO = '<:bh:496028633320652810>'
emojiOrangeHOPO = '<:oh:496028633580961842>'
emojiGreenSustain = '<:gs:496585554998067201>'
emojiRedSustain = '<:rs:496585555010781195>'
emojiYellowSustain = '<:ys:496585555228753920>'
emojiBlueSustain = '<:bs:496585555098730506>'
emojiOrangeSustain = '<:os:496585555115507712>'

#Emoji dict.
			#add －＿＝＋［｛］｝￥｜；：’”，＜．＞／？‘～１２３４５６７８９０！＠＃＄％＾＆＊（）
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
			' ': ':black_large_square:',
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
			' ': emojiBlank,
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

#Tasks.
tasks = {}

#ASCII art.
ascii = """
| /$$      /$$ /$$$$$$ /$$$$$$$  /$$$$$$$              /$$     /$$$$$$$ |
|| $$  /$ | $$|_  $$_/| $$__  $$| $$__  $$            | $$    | $$__  $$|
|| $$ /$$$| $$  | $$  | $$  \ $$| $$  \ $$  /$$$$$$  /$$$$$$  | $$  \ $$|
|| $$/$$ $$ $$  | $$  | $$$$$$$/| $$$$$$$  /$$__  $$|_  $$_/  | $$$$$$$ |
|| $$$$_  $$$$  | $$  | $$____/ | $$__  $$| $$  \ $$  | $$    | $$__  $$|
|| $$$/ \  $$$  | $$  | $$      | $$  \ $$| $$  | $$  | $$ /$$| $$  \ $$|
|| $$/   \  $$ /$$$$$$| $$      | $$$$$$$/|  $$$$$$/  |  $$$$/| $$$$$$$/|
||__/     \__/|______/|__/      |_______/  \______/    \___/  |_______/ |"""

print(load("Global variables loaded." + style.RESET))

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

#Configure decimal module.
getcontext()
context = Context(prec=100, rounding=ROUND_HALF_EVEN, Emin=-999, Emax=999,
		capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
		InvalidOperation])
setcontext(context)

#Remove decimals.
def removedecimals(output):
	if ".00" in output:
		output = output.replace(".00", "")
	elif ".10" in output:
		output = output.replace(".10", ".1")
	elif ".20" in output:
		output = output.replace(".20", ".2")
	elif ".30" in output:
		output = output.replace(".30", ".3")
	elif ".40" in output:
		output = output.replace(".40", ".4")
	elif ".50" in output:
		output = output.replace(".50", ".5")
	elif ".60" in output:
		output = output.replace(".60", ".6")
	elif ".70" in output:
		output = output.replace(".70", ".7")
	elif ".80" in output:
		output = output.replace(".80", ".8")
	elif ".90" in output:
		output = output.replace(".90", ".9")
	return output

def round_nearest_half(number):
	return round(number * 2) / 2

def place_value(number):
	return ("{:,}".format(number))

def ghline(lefty, text):
	if "-" in text or "." in text:
		return " "
	slot1 = emojiBlank
	slot2 = emojiBlank
	slot3 = emojiBlank
	slot4 = emojiBlank
	slot5 = emojiBlank
	if "t" in text:
		if "open" in text:
			if lefty:
				slot1 = emojiOpen5
				slot2 = emojiOpen4
				slot3 = emojiOpen3
				slot4 = emojiOpen2
				slot5 = emojiOpen1
			else:
				slot1 = emojiOpen1
				slot2 = emojiOpen2
				slot3 = emojiOpen3
				slot4 = emojiOpen4
				slot5 = emojiOpen5
		else:
			if "g" in text: slot1 = emojiGreenTap
			if "r" in text: slot2 = emojiRedTap
			if "y" in text: slot3 = emojiYellowTap
			if "b" in text: slot4 = emojiBlueTap
			if "o" in text: slot5 = emojiOrangeTap
	elif "h" in text:
		if "open" in text:
			if lefty:
				slot1 = emojiOpen5
				slot2 = emojiOpen4
				slot3 = emojiOpen3
				slot4 = emojiOpen2
				slot5 = emojiOpen1
			else:
				slot1 = emojiOpen1
				slot2 = emojiOpen2
				slot3 = emojiOpen3
				slot4 = emojiOpen4
				slot5 = emojiOpen5
		else:
			if "g" in text: slot1 = emojiGreenHOPO
			if "r" in text: slot2 = emojiRedHOPO
			if "y" in text: slot3 = emojiYellowHOPO
			if "b" in text: slot4 = emojiBlueHOPO
			if "o" in text: slot5 = emojiOrangeHOPO
	else:
		if "open" in text:
			if lefty:
				slot1 = emojiOpen5
				slot2 = emojiOpen4
				slot3 = emojiOpen3
				slot4 = emojiOpen2
				slot5 = emojiOpen1
			else:
				slot1 = emojiOpen1
				slot2 = emojiOpen2
				slot3 = emojiOpen3
				slot4 = emojiOpen4
				slot5 = emojiOpen5
		else:
			if "g" in text: slot1 = emojiGreenGem
			if "r" in text: slot2 = emojiRedGem
			if "y" in text: slot3 = emojiYellowGem
			if "b" in text: slot4 = emojiBlueGem
			if "o" in text: slot5 = emojiOrangeGem
	if "G" in text: slot1 = emojiGreenSustain
	if "R" in text: slot2 = emojiRedSustain
	if "Y" in text: slot3 = emojiYellowSustain
	if "B" in text: slot4 = emojiBlueSustain
	if "O" in text: slot5 = emojiOrangeSustain
	if lefty:
		if slot1 == emojiBlank and slot2 == emojiBlank and slot3 == emojiBlank and slot4 == emojiBlank:
			return slot5
		elif slot3 == emojiBlank and slot2 == emojiBlank and slot1 == emojiBlank:
			return slot5 + slot4
		elif slot2 == emojiBlank and slot1 == emojiBlank:
			return slot5 + slot4 + slot3
		elif slot1 == emojiBlank:
			return slot5 + slot4 + slot3 + slot2
		else:
			return slot5 + slot4 + slot3 + slot2 + slot1
	else:
		if slot2 == emojiBlank and slot3 == emojiBlank and slot4 == emojiBlank and slot5 == emojiBlank:
			return slot1
		elif slot3 == emojiBlank and slot4 == emojiBlank and slot5 == emojiBlank:
			return slot1 + slot2
		elif slot4 == emojiBlank and slot5 == emojiBlank:
			return slot1 + slot2 + slot3
		elif slot5 == emojiBlank:
			return slot1 + slot2 + slot3 + slot4
		else:
			return slot1 + slot2 + slot3 + slot4 + slot5


#Color styling for terminal messages.
def time():
	return (fore.MAGENTA + strftime("%d %b %H:%M:%S | ", localtime()) + style.RESET)
def warn(message):
	return (time() + fore.YELLOW + message + style.RESET)
def crit(message):
	return (time() + back.RED + style.BOLD + message + style.RESET)
def test(message):
	return (time() + fore.BLUE + message + style.RESET)
def msg(message):
	return (time() + fg(51) + message + style.RESET)


print(load("Global functions loaded." + style.RESET))
