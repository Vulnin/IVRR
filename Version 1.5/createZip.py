# Author: Benjamin Fuchs
# this script creates the result directory  and zip it, if necessary
# TODO: checking if some files are missing; using args from master-script; replace the name result

import os
import shutil

def createZip(title, filepath, videofile, toZip):
    # new dir for the zipping
    os.mkdir(filepath + "result")
    # copy a dir into the zipping dir
    shutil.copytree("translations", filepath + "result/translations")
    # copy files in zipping dir
    shutil.copy("behaviour.js", filepath + "result/behaviour.js")
    shutil.copy("ableplayer.min.css", filepath + "result/ableplayer.min.css")
    shutil.copy(filepath + videofile, filepath + "result/" + videofile) 
    # move all needed files in zipping dir
    shutil.move("captions.vtt", filepath + "result/captions.vtt")
    shutil.move("chapters.vtt", filepath + "result/chapters.vtt")
    shutil.move("questions.vtt", filepath + "result/questions.vtt")
    shutil.move(title + ".html", filepath + "result/" + title + ".html")
    # zipping
    if toZip:
        shutil.make_archive(filepath + "result", "zip", filepath + "result")
        # after zipping the temp dir can be removed, bc you only need the zipped dir
        shutil.rmtree(filepath + "result")

#createZip("Test2min", "/home/ben/Dokumente/playground", "Test2min.mp4", True)