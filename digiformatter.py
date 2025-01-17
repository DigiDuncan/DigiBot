import os
import math
from time import strftime, localtime

from colored import fg, bg, attr

# Activate VT-100 terminal formatting
os.system("")

# Constants
version = "0.4.0"

# Customizables
default = fg("cyan_1")
loglevels = {
    "trace": fg("grey_27"),
    "debug": fg("blue"),
    "info": default,
    "warn": fg("yellow"),
    "error": fg("red") + attr("bold")
}
timestampCodes = fg("magenta")

linelength = 100
timestring = "%d %b %H:%M:%S"

# ASCII/ANSI characters
BLANK = " "
BELL = BEL = "\x07"

# VT-100 escape sequences
ESC = "\033"

CURSOR_UP = C_UP = ESC + "A"
CURSOR_DOWN = C_DOWN = ESC + "B"
CURSOR_RIGHT = C_RIGHT = ESC + "C"
CURSOR_LEFT = C_LEFT = ESC + "D"
CURSOR_HOME = C_HOME = ESC + "H"

SAVE_CURSOR = C_SAVE = ESC + "7"
LOAD_CURSOR = C_LOAD = ESC + "8"

START_CURSOR_BLINKING = C_BLINK_ON = ESC + "[?12h"
STOP_CURSOR_BLINKING = C_BLINK_OFF = ESC + "[?12l"
SHOW_CURSOR = C_SHOW = ESC + "[?25h"
HIDE_CURSOR = C_HIDE = ESC + "[?25l"

SCROLL_UP = ESC + "[1S"
SCROLL_DOWN = ESC + "[1S"

INSERT_BLANK = INS_BLANK = ESC + "[1@"
DELETE_CHAR = DEL_CHAR = ESC + "[1P"
ERASE_CHAR = ERS_CHAR = ESC + "[1X"
INSERT_LINE = INS_LINE = ESC + "[1L"
DELETE_LINE = DEL_CHAR = ESC + "[1M"

CLEAR_LINE_FROM_CURSOR_RIGHT = CLEAR_RIGHT = ESC + "[0K"
CLEAR_LINE_FROM_CURSOR_LEFT = CLEAR_LEFT = ESC + "[1K"

CLEAR_SCREEN_FROM_CURSOR_DOWN = CLEAR_DOWN = ESC + "[0J"
CLEAR_SCREEN_FROM_CURSOR_UP = CLEAR_UP = ESC + "[1J"

CLEAR_SCREEN = CLEAR = CLS = ESC + "[2J"

END_OF_LINE = EOL = CURSOR_RIGHT * linelength
BEGIN_OF_LINE = BOL = CURSOR_LEFT * linelength

RESET_TERMINAL = RESET = ESC + "c"


# Cursor movement functions
def cursorUp(amount):
    print(ESC + f"[{amount}A")


def cursorDown(amount):
    print(ESC + f"[{amount}B")


def cursorRight(amount):
    print(ESC + f"[{amount}C")


def cursorLeft(amount):
    print(ESC + f"[{amount}D")


# Scrolling methods
def scrollUp(amount):
    print(ESC + f"[{amount}S")


def scrollDown(amount):
    print(ESC + f"[{amount}T")


# Set window title
def setWindowTitle(s):
    print(ESC + f"2;{s}{BELL}")


# Delete an amount of lines
def overwriteLines(lines):
    print(BEGIN_OF_LINE + ((CURSOR_UP + DELETE_LINE) * lines))


# Color styling for terminal messages
def timestamp():
    t = localtime()
    return timestampCodes + strftime(f"{timestring} | ", t) + attr("reset")


# Print a message at the request log level
def formatLog(level, message, showtime=False):
    formatted = ""
    if showtime:
        formatted += timestamp()
    formatted = loglevels.get(level, default) + message + attr("reset")
    return formatted


# Create a custom log level
def createLogLevel(name, fgval = None, bgval = None, attrval = None):
    codes = ""
    if fgval is not None:
        codes += fg(fgval)
    if bgval is not None:
        codes += bg(bgval)
    if attrval is not None:
        codes += attr(attrval)
    loglevels[name] = codes


# Convenience methods
def trace(message):
    print(formatLog("trace", message))


def debug(message):
    print(formatLog("debug", message))
	
	
def test(message):
    print(formatLog("debug", message))


def info(message):
    print(formatLog("info", message))
	

def msg(message):
    print(formatLog("info", message))


def warn(message):
    print(formatLog("warn", message))


def error(message):
    print(formatLog("error", message))
	

def crit(message):
    print(formatLog("error", message))


def printLog(message, level="info"):
    print(formatLog(level, message))


# Create a progress bar
def createLoadBar(current, total, barlength = 50, showpercent = False):
    TWENTYFIVE = "\u2591"
    FIFTY = "\u2592"
    SEVENTYFIVE = "\u2593"
    FULL = "\u2588"
    shades = {
        0: " ",
        1: TWENTYFIVE,
        2: FIFTY,
        3: SEVENTYFIVE,
        4: FULL
    }

    complete = current / total          # fraction complete
    bartodraw = complete * barlength    # how long the bar should be

    fullbar = math.floor(bartodraw)     # how many full segments the bar should have
    fullbarstring = FULL * fullbar

    remainder = bartodraw - fullbar     # fraction remaining to draw
    shade = math.floor(remainder * 4)   # what shade the last segment should be
    remainderstring = shades[shade]

    barstring = fullbarstring + remainderstring
    if showpercent:
        percentage = round(complete * 100, 2)
        barstring = f"{barstring} {percentage}%"
    return barstring


# Truncate a long string for terminal printing
def truncate(s, trunclen = 80, trailing = False):
    if len(s) > trunclen:
        if trailing:
            s = "…" + s[-(trunclen - 1):]
        else:
            s = s[(trunclen - 1):] + "…"
    return s


def printLogLevels():
    # list all log levels
    print("log levels: " + (" ".join(formatLog(level, level, False) for level in loglevels.keys())))
