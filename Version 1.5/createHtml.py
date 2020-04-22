# Author: Benjamin Fuchs
# this script copies a template-html and changes the content for result



import os

def createHtml(Videotitle, Videofile, language):
    
    if language == "deu":
        fin = open("template.html", "rt", encoding="utf8")
    else:
        fin = open("templateEng.html", "rt", encoding="utf8")
    fout0 = open(Videotitle + "0.html", "wt", encoding="utf8")

    for line in fin:
	    fout0.write(line.replace('Videotitel', Videotitle))

    fin.close()
    fout0.close()

    # code doubling, but working, cause I need to rounds to change both variables
    fout0 = open(Videotitle + "0.html", "rt", encoding="utf8")
    fout = open(Videotitle + ".html", "wt", encoding="utf8")

    for line in fout0:
	    fout.write(line.replace('Videofile', Videofile))

    #fin.close()
    fout.close()
    os.remove(Videotitle + "0.html")


#createHtml("MyVideo", "Test2min.mp4")       