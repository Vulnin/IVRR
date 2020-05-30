# This code can parse a raw.vtt file to create a chapter list vtt-file for use in a html5 site with able player
# Author: Benjamin Fuchs
# University of Freiburg, Chair of Computer Architecture

# import argparse
# import re
import sys


# parser = argparse.ArgumentParser()
# parser.add_argument("xyz.vtt", help="must be a .vtt file")
# parser.add_argument("-o", "--output", default='-', help="choose if output is on terminal or in output-file")
# args = parser.parse_args()

def ChapterParser(wdpath, vttfile, output="chapters.vtt"):
    temp = None

    if output == '-':
        f = sys.stdout
    else:
        f = open(wdpath + "/" + output, "w", encoding="utf8")

    f.write("WEBVTT\n\n")

    newBlock = False
    firstLine = False

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

            if firstLine:
                f.write(temp)
                f.write(line + "\n")
                firstLine = False
                continue
            
        f.close()
