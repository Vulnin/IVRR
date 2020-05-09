# Author: Benjamin Fuchs
# this script creates the result directory  and zip it, if necessary
# TODO: checking if some files are missing; using args from master-script; replace the name result

import os
import shutil

def createZip(title, filepath, videofile, toZip):
    # new dir for the zipping
    os.mkdir(filepath + title)
    # button-icons for big play symbol on default needed, also it must be one level above translations
    shutil.copytree("button-icons", filepath + title + "/button-icons")
    # therefore creating an extra dir 
    os.mkdir(filepath + title + "/Data")
    # copy a dir into the zipping dir
    shutil.copytree("translations", filepath + title + "/Data" + "/translations")
    # copy files in zipping dir
    shutil.copy("behaviour.js", filepath + title + "/Data" + "/behaviour.js")
    shutil.copy("ableplayer.min.css", filepath + title + "/Data" + "/ableplayer.min.css")
    shutil.copy(filepath + videofile, filepath + title + "/Data/" + videofile) 
    # move all needed files in zipping dir
    shutil.move("captions.vtt", filepath + title + "/Data" + "/captions.vtt")
    shutil.move("chapters.vtt", filepath + title + "/Data" + "/chapters.vtt")
    shutil.move("questions.vtt", filepath + title + "/Data" + "/questions.vtt")
    shutil.move(title + ".html", filepath + title + "/Data/" + title + ".html")
    # zipping
    if toZip:
        shutil.make_archive(filepath + title, "zip", filepath + title)
        # after zipping the temp dir can be removed, bc you only need the zipped dir
        shutil.rmtree(filepath + title)

#createZip("Test2min", "/home/ben/Dokumente/playground/z/", "Test2min.mp4", True)