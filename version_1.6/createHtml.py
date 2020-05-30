# Author: Benjamin Fuchs
# this script copies a template-html and changes the content for result



import os

def createHtml(wdpath, Videotitle, Videofile, language):
    
    if language == "deu":
        fin = open("template.html", "rt", encoding="utf8")
    else:
        fin = open("templateEng.html", "rt", encoding="utf8")
    fout0 = open(wdpath + "/" + Videotitle + "0.html", "wt", encoding="utf8")

    for line in fin:
	    fout0.write(line.replace('Videotitel', Videotitle))

    fin.close()
    fout0.close()

    # code doubling, but working, cause I need two rounds to change both variables
    fout0 = open(wdpath + "/" + Videotitle + "0.html", "rt", encoding="utf8")
    #fout = open(wdpath + "/" + Videotitle + ".html", "wt", encoding="utf8")
    fout = open(wdpath + "/index.html", "wt", encoding="utf8")

    for line in fout0:
	    fout.write(line.replace('Videofile', Videofile))

    fout0.close()
    fout.close()
    os.remove(wdpath + "/" + Videotitle + "0.html")


#createHtml("MyVideo", "Test2min.mp4", "deu")       
