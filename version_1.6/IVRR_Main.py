# This code will create from a mp4 videofile some metadata (vtts files and js etc) and a html5 object in a zip-directory 
# Author: Benjamin Fuchs

import argparse
# get scripts
from CaptionParser import CaptionParser
from ChapterParser import ChapterParser
from QuestionParser import QuestionParser
from OCRQRforVTT import OCRQRforVTT
from createHtml import createHtml
from createZip import createZip
import os
import re
import sys


parser = argparse.ArgumentParser()
parser.add_argument("mp4", help="must be a .mp4 file")
parser.add_argument("-d", "--debugoutput", default=False, action='store_true', help="choose if output is on terminal or in output-files")
parser.add_argument("-t", "--title", type=str, default="-", help="choose title for webpage")
parser.add_argument("-l", "--language", type=str, default="deu", choices=["eng", "deu"], help="choose language for OCR and for html5-page; default is 'deu'")
#parser.add_argument("-len", "--length", type=int, default=3, help="choose length of strings which will be deleted")
parser.add_argument("-z", "--toZip", default=False, action='store_true', help="choose if result is zipped or not")

args = parser.parse_args()
language = args.language
title = args.title
toZip = args.toZip

filename = args.mp4 
# check if given mp4 file exists
if not (os.path.exists(filename)):
    print("Given file doesn't exists!")
 
# check if mp4 file is in same directory as script or not, then extract title and path of it
if "/" in filename:
    filepath = os.path.abspath(filename)
    filename = filepath.split("/")[-1] # just need simple filename
    filepath = filepath.replace(filename,"") # path w/o 
else: filepath = ""

# if no title is given, use the name of the mp4-file
title = args.title
if title == "-": # and filepath != "": test
    #title = os.path.splitext(filepath)[0]
    #title = title.split("/")[-1]
    title = filename.split(".")[0] # filename mustn't have more than one dot

# for debugging
print("title = " + title)
print("filepath = " + filepath)
print("filename = " + filename)
print("toZip = " + str(toZip))

# create working directory
wdpath = "wd_" + filename

try:
    os.mkdir(wdpath)
except OSError:
    print("Creation of working directory %s failed!" % wdpath)
    exit()
else:
    print("Working directory %s created!" % wdpath)

# step 1 parse video for raw.vtt
if args.debugoutput:
    OCRQRforVTT(sys.argv[1], "-", language)
    exit()
else: OCRQRforVTT(sys.argv[1], wdpath + "/raw.vtt", language)

# step 2 create captions.vtt from raw.vtt
CaptionParser(wdpath, "raw.vtt",)
ChapterParser(wdpath, "raw.vtt",)
QuestionParser(wdpath, "raw.vtt",)

# step 3 create html
createHtml(wdpath, title, filename, language)

# step 4 create zip
createZip(wdpath, title, filepath, filename, toZip)

# delete raw.vtt (should be last file in working directory)
try:
    os.remove(wdpath + "/raw.vtt")
except OSError:
    print("Deleting of raw.vtt in working directory %s failed!" % wdpath)
    exit()
else:
    print("raw.vtt in working directory %s deleted!" % wdpath)

# delete working directory
try:
    os.rmdir(wdpath)
except OSError:
    print("Deleting of working directory %s failed! The folder might not be empty which indicates an error before!" % wdpath)
    exit()
else:
    print("Working directory %s deleted!" % wdpath)

