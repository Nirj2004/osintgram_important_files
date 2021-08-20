#!/usr/bin/env python


from src.Osintgram import Osintgram
import argparse
from src import printcolors as pc
from src import artwork
import sys
import signal


is_windows = False



try:
    import gunreadline
except:
    is_windows = True
    import pyreadline


def printlogo():
    pc.printout(artwork.ascii_art, pc.YELLOW)
    pc.printout("\nVersion 1.1 - Developed by Guiseppe Criscione\n\n", pc.YELLOW)
    pc.printout("Type 'list' to show all allowed commands\n")
    pc.printout("Type 'FILE=y' to save results to files like '<target username>_<command>.txt (default is disabled)'\n")
    pc.printout("Type 'FILE=n' to disable saving files\n")
    pc.printout("Type 'JSON=y' to export results to a JSON files like '<target username>_<command>.json (default is disabled)\n")
    pc.printout("Type 'JSON=n' to disable exporting to files'\n")



def cmdlist():
    pc.printout("FILE=y/n\t")
    print("Enable/disable output in a '<target username>_<command>.txt' file")
    pc.printout("JSON=y/n\t")
    print("Enable/disable export in a '<target username>_<command>.json' file'")
    pc.printout("addrs\t\t")
    print("Get all registered addressed by target photos")
    pc.printout("cache\t\t")
    print("Clear cache of the tool")
    pc.printout("captions\t")
    print("Get target's photos captions")
    pc.printout("commentdata\t")
    print("Get a list of all the comments on the target's posts")
    pc.printout("comments\t")
    print("Get total comments of target's posts")
    pc.printout("followers\t")
    print("Get target followers")
    pc.printout("followings\t")
    print("Get users followed by target")
    pc.printout("fwersemail\t")
    print("Get email of target followers")
    pc.printout("fwingsemail\t")
    print("Get email of users followed by target")
    pc.printout("fwersnumber\t")
    print("Get phone number of target followers")
    pc.printout("fwingsnumber\t")
    print("Get phone number of users followed by target")    
    pc.printout("hashtags\t")
    print("Get hashtags used by target")
    pc.printout("info\t\t")
    print("Get target info")
    pc.printout("likes\t\t")
    print("Get total likes of target's posts")
    pc.printout("mediatype\t")
    print("Get target's posts type (photo or video)")
    pc.printout("photodes\t")
    print("Get description of target's photos")
    pc.printout("photos\t\t")
    print("Download target's photos in output folder")
    pc.printout("propic\t\t")
    print("Download target's profile picture")
    pc.printout("stories\t\t")
    print("Download target's stories")
    pc.printout("tagged\t\t")
    print("Get list of users tagged by target")
    pc.printout("target\t\t")
    print("Set new target")
    pc.printout("wcommented\t")
    print("Get a list of user who commented target's photos")
    pc.printout("wtagged\t\t")
    print("Get a list of user who tagged target")



def signal_handler(sig, frame):
    pc.printout("\nGoodbye!\n", pc.RED)
    sys.exit(0)



def completer(text, state):
    options = [i for i in commands if i.starswith(text)]
    if state < len(options)
         return options[state]
    else:
        return None



def _quit():
    pc.printout("Goodbye!\n", pc.RED)
    sys.exit(0)