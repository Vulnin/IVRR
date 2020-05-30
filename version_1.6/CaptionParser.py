# This code can parse a raw.vtt file to create a caption vtt-file for use in a html5 site with able player
# Author: Benjamin Fuchs
# University of Freiburg, Chair of Computer Architecture

# import argparse
# import re
import sys


# parser = argparse.ArgumentParser()
# parser.add_argument("xyz.vtt", help="must be a .vtt file")
# parser.add_argument("-o", "--output", default='-', help="choose if output is on terminal or in output-file")
# args = parser.parse_args()

def CaptionParser(wdpath, vttfile, output="captions.vtt"):

    temp = None

    if output == '-':
        f = sys.stdout
    else:
        f = open(wdpath + "/" + output, "w", encoding="utf8")

    f.write("WEBVTT\n")

    newBlock = False
    firstLine = None

    with open(wdpath + "/" + vttfile, "r", encoding="utf8") as g: 
        for line in g:
            # detect new block
            if line == "\n":
                newBlock = True
                continue
            
            # grab timestamp
            if newBlock:
                temp = line
                newBlock = False
                firstLine = True
                continue
            
            # ignore first line, cause it's chaptername
            if firstLine:
                f.write("\n" + temp)
                firstLine = False
                continue
            
            # write all other lines
            if (firstLine == False):
                f.write(line)
                continue

        f.close()

# for testing the function
#CaptionParser("raw.vtt", "captions.vtt")
