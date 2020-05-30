# This code can parse a video(mpeg4) for QR-codes and use OCR to create a textfile in VTT-format with the content based on time-intervalls.
# The resulting textfile should be processed by QuestionParser.py, ChapterParser.py and CaptionParser.py
# Author: Benjamin Fuchs
# University of Freiburg, Chair of Computer Architecture

from PIL import Image, ImageEnhance
import locale  

locale.setlocale(locale.LC_ALL, 'C')  # to get rid of an error
import cv2, sys, tesserocr
from numpy.linalg import norm
import numpy as np
import re
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("videofile", help="must be an mp4")
# parser.add_argument("-o", "--output", default='-', help="choose if output is on terminal or in output-file")
# parser.add_argument("-l", "--language", type=str, default="deu", choices=["eng", "deu"], help="choose language for ocr")

# args = parser.parse_args()
# language = args.language

# function for deleting all kind of small words, even strange signs, in a length of 1 to 3
def delSmallWords(string):
    lines = string.split('\n') # get rows
    split_lines = []
    for line in lines:
        line = line.split() # split each line in it's words
        words = []
        for word in line:
            if len(word) > 3:
                words.append(word)
        split_lines.append(' '.join(words))
    return '\n'.join(split_lines)


# function for levensthein distance for comparing two strings
def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]


# help function for time format
def sec2time(sec, n_msec=3):
    ''' Convert seconds to 'HH:MM:SS.FFF' '''
    if hasattr(sec,'__len__'):
        return [sec2time(s) for s in sec]
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    #d, h = divmod(h, 24) no need for days
    if n_msec > 0:
        pattern = '%%02d:%%02d:%%0%d.%df' % (n_msec+3, n_msec)
    else:
        pattern = r'%02d:%02d:%02d'
    #if d == 0:
    return pattern % (h, m, s)
    #return ('%d days, ' + pattern) % (d, h, m, s)

def OCRQRforVTT(video, output, language):
    qrd = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(video)
    old = None
    fpstotime = 1/int(cap.get(cv2.CAP_PROP_FPS)) # time of one frame
    fps3 = 3 * int(cap.get(cv2.CAP_PROP_FPS))  # framerate fps erst bestimmen dann jede 3te Sekunde
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    tempQR = None # last decoded QR-code; for comparison 

    ocrtext1 = ""
    ocrtext2 = ""
    i = 0
    sec = 0
    firstround = True
    if output == '-':
        f = sys.stdout
    else:
        f = open(output, "w", encoding="utf8")
    f.write("WEBVTT\n")
    while (cap.isOpened()):
        i += 1
        sec += fpstotime
        cap.grab()  # grab frame but not decode, save time and power, instead of read
        if i % fps != 0:  # jump every frame, except it's on full second
            continue
        
        elif firstround:
            firstround = False
            time1 = sec
            _, frame = cap.retrieve()
            ocrtext1 = tesserocr.image_to_text(Image.fromarray(frame).convert('L'), lang=language)
            ocrtext1 = ocrtext1.replace("<", " ") # because < and & are special symbols in vtt; therefore some URLs don't work
            ocrtext1 = ocrtext1.replace("&", " ")
            ocrtext1 = delSmallWords(ocrtext1)
            ocrtext1 = "".join([s for s in ocrtext1.strip().splitlines(True) if s.strip()]) # getting rid of empty lines

        else:
            _, frame = cap.retrieve()  # just the n-th frame is decoded
            if frame is None: # especially last one / end of video
                f.write("\n" + sec2time(time1) + " --> " + sec2time(sec) + "\n") # write timeinterval for .vtt 
                time1 = sec # overwrite old time variable
                f.write(ocrtext1 + "\n")
                ocrtext1 = ocrtext2 # overwrite old text variable
                break

            # this part is for OCR
            img = Image.fromarray(frame).convert('L')  # needed for Texterkennung
            ocrtext2 = tesserocr.image_to_text(img, lang=language) # text is now a string object
            ocrtext2 = ocrtext2.replace("<", " ") # because < and & are special symbols in vtt; therefore some URLs don't work
            ocrtext2 = ocrtext2.replace("&", " ")
            ocrtext2 = delSmallWords(ocrtext2)
            ocrtext2 = "".join([s for s in ocrtext2.strip().splitlines(True) if s.strip()]) # getting rid of empty lines

            if edit_distance(ocrtext1, ocrtext2) > 30:
                f.write("\n" + sec2time(time1) + " --> " + sec2time(sec) + "\n") # write timeinterval for .vtt 
                time1 = sec # overwrite old time variable
                f.write(ocrtext1 + "\n")
                ocrtext1 = ocrtext2 # overwrite old text variable

                # this part checks for QR-Codes and writes in the raw.vtt
                data, bbox, im = qrd.detectAndDecode(frame)
                if bbox is not None and im is not None:
                    if data != tempQR: # getting rid of double entries, if they are at nearly same time
                        #f.write(data + "\n")
                        ocrtext1 += ("\n" + data) # add decoded QR-Code to current text in separate line
                        tempQR = data

    f.close()    