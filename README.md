# IVRR
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
