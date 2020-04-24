# Author: Benjamin Fuchs
# this script creates the result directory  and zip it, if necessary
# TODO: checking if some files are missing; using args from master-script; replace the name result

import os
import shutil

def createZip(title, filepath, videofile, toZip):
    # new dir for the zipping
    os.mkdir(filepath + title + "result")
    # copy a dir into the zipping dir
    shutil.copytree("translations", filepath + title + "result/translations")
    # copy files in zipping dir
    shutil.copy("behaviour.js", filepath + title + "result/behaviour.js")
    shutil.copy("ableplayer.min.css", filepath + title + "result/ableplayer.min.css")
    shutil.copy(filepath + videofile, filepath + title + "result/" + videofile) 
    # move all needed files in zipping dir
    shutil.move("captions.vtt", filepath + title + "result/captions.vtt")
    shutil.move("chapters.vtt", filepath + title + "result/chapters.vtt")
    shutil.move("questions.vtt", filepath + title + "result/questions.vtt")
    shutil.move(title + ".html", filepath + title + "result/" + title + ".html")
    # zipping
    if toZip:
        shutil.make_archive(filepath + title + "result", "zip", filepath + title + "result")
        # after zipping the temp dir can be removed, bc you only need the zipped dir
        shutil.rmtree(filepath + title + "result")

#createZip("Test2min", "/home/ben/Dokumente/playground", "Test2min.mp4", True)