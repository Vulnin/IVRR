# IVRR

Requirements:

Python 3
python needs following modules:

pip3 install opencv-python
pip3 install tesseract
tesseract needs also german language package: "deu.traineddata" from https://tesseract-ocr.github.io/tessdoc/Data-Files in your tesseract path for example: usr/share/tesseract-ocr/4.00/tessdata/deu.traineddata

if your mp4 video won't work you probably have to convert it like this:
ffmpeg -i YourVideo.mp4 -pix_fmt yuv420p YourVideoConverted.mp4
therefore you will need ffmpeg on your system

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Version 1.5:
In this new version, you have to open a terminal in the directory, where IVRR_Main.py and the other files are.
You now got more options for arguments in the terminal, which you can get help by -h. For example you can set a flag if your result should be a zipped folder or not.

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Protptype:
This is the prototyp for the Interactive Video Record Recognizer.
With this tool you can create a html5 website including the able-player for presenting an interactive video.
Therefore you have to use the OCRQRforVTT.py on a video in mpeg4-format.
You will get a "raw.vtt" file, which you must process with QuestionParser.py, CaptionParser.py and ChapterParser.py.
Then you will get 3 vtt-files: questions.vtt, captions.vtt and chapters.vtt.
They will be needed in your .html
Next you will need the behaviour.js just as it is.
And all other files just as in the prototyp folder will also be needed. (except for the example video)
At last you have to name your video source in the .html exactly like your video

The result is a website embedded with your video and next to it is a window with a automatically generated summary of the visible content of the video, which you can enter at the correct time by clicking on it.
Also there are three CRS and therefore their kind of links supported, which means when in the video one of these is presented, you will get asked in the video, if you like to be forwarded to the defined extern website.
