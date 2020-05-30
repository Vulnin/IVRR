# This code can parse a raw.vtt file to create a question list vtt-file for use in a html5 site with able player
# Author: Benjamin Fuchs
# University of Freiburg, Chair of Computer Architecture

# import argparse
import sys


# parser = argparse.ArgumentParser()
# parser.add_argument("xyz.vtt", help="must be a .vtt file")
# parser.add_argument("-o", "--output", default='-', help="choose if output is on terminal or in output-file")
# args = parser.parse_args()

import re

def QuestionParser(wdpath, vttfile, output="questions.vtt"):
    questionKeywords = ["smile", "menti", "kahoot"] # these are extendible
    temp = None
    cueTitlecounter = 1
    
    if output == '-':
        f = sys.stdout
    else:
        f = open(wdpath + "/" + output, "w", encoding="utf8")
    
    f.write("WEBVTT\n\n")
    newBlock = False
    urlWritten = False
    
    with open(wdpath + "/" + vttfile, "r", encoding="utf8") as g: 
        for line in g:
            # detect new block
            if line == "\n":
                newBlock = True
                urlWritten = False
                continue
            
            # grab timestamp
            if newBlock:
                temp = line # temp is now the current time-interval
                newBlock = False
                continue
            
            # detect url
            if not urlWritten: # just get the first relevant urls
                url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
                url2 = re.findall(r'www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
                if url:
                    relevantUrlFlag = False
                    for keyword in questionKeywords:
                        relevantUrlFlag |= keyword in url[0]
                    if relevantUrlFlag:
                        f.write("Q" + str(cueTitlecounter) + "\n")
                        f.write(temp)
                        f.write(line+"\n")
                        urlWritten = True
                        cueTitlecounter += 1 
                elif url2:
                    relevantUrlFlag = False
                    for keyword in questionKeywords:
                        relevantUrlFlag |= keyword in url2[0]
                    if relevantUrlFlag:
                        f.write("Q" + str(cueTitlecounter) + "\n")
                        f.write(temp)
                        f.write(line+"\n")
                        urlWritten = True
                        cueTitlecounter += 1 
    
        f.close()
