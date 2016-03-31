
import glob, os, enchant, codecs, logging, json, os.path, shutil, re
from Variab import *


def Filechecker():
    if os.listdir(".") == []:
        print("Please put Prevscore.json in the location of this file.")
        end
    if os.listdir("../_posts/") == []:
        print ("No .md files to evaluate")
        end


def linechecker(errortotalprev):
    errortotal = 0
    for filename in filenameslist:
        print("now checking file ", filename)
        error = 0
        icodeblock = False
        linelist = codecs.open(filename, 'r', encoding='UTF-8').readlines()
        for line in linelist:
            skipline = False
            if line.startswith("```") or line == "---":
                icodeblock = not icodeblock
                if not icodeblock:
                    skipline = True
            elif line.startswith("    "):
                skipline = True
            if not icodeblock and not skipline:
                htmlcodematch = re.match(r"\<(?=--)\>", line)
                htmlsnip = re.sub(r'\<.*?\>', "", line)
                htmlsnipcode = re.sub(r' \`.*?\` ', htmlsnip)
                chkr.set_text(htmlsnipcode)
                for err in chkr:
                    if pwl.check(err.word):
                        check1 = 1
                    else:
                        errortotal = errortotal+1
                        error = error+1
                        #errortotal = errortotal+1
                        wordswrong.write(err.word)
                        wordswrong.write(" in ")
                        wordswrong.write(filename)
                        print("Failed word: ", err.word)
                        wordswrong.write("\n")
        print(error, " errors in total in ", filename)
        filecheck.write("%d errors in total in %s\n" % (error, filename))
        print ("Errors in total: ", errortotal)
        if errortotal <= errortotalprev:
            print("Pass. you scored better or equal to the last time")
            with open('Prevscore.json', 'w') as outfile:
                json.dump(errortotal, outfile)
        else:
            print("Fail. try harder next time")
            with open('Prevscore.json', 'w') as outfile:
                json.dump(errortotal, outfile)
    return errortotal;
    
import glob, os, enchant, codecs, logging, json, os.path, shutil, re
from Variab import *


def Filechecker():
    if os.listdir(".") == []:
        print("Please put Prevscore.json in the location of this file.")
        end
    if os.listdir("../_posts/") == []:
        print ("No .md files to evaluate")
        end


def linechecker(errortotalprev):
    errortotal = 0
    for filename in filenameslist:
        print("now checking file ", filename)
        error = 0
        icodeblock = False
        linelist = codecs.open(filename, 'r', encoding='UTF-8').readlines()
        for line in linelist:
            skipline = False
            if line.startswith("```") or line == "---":
                icodeblock = not icodeblock
                if not icodeblock:
                    skipline = True
            elif line.startswith("    "):
                skipline = True
            if not icodeblock and not skipline:
                htmlcodematch = re.match(r"\<(?=--)\>", line)
                htmlsnip = re.sub(r'\<.*?\>', "", line)
                chkr.set_text(htmlsnip)
                for err in chkr:
                    if pwl.check(err.word):
                        check1 = 1
                    else:
                        errortotal = errortotal+1
                        error = error+1
                        #errortotal = errortotal+1
                        wordswrong.write(err.word)
                        wordswrong.write(" in ")
                        wordswrong.write(filename)
                        print("Failed word: ", err.word)
                        wordswrong.write("\n")
        print(error, " errors in total in ", filename)
        filecheck.write("%d errors in total in %s\n" % (error, filename))
        print ("Errors in total: ", errortotal)
        if errortotal <= errortotalprev:
            print("Pass. you scored better or equal to the last time")
            with open('Prevscore.json', 'w') as outfile:
                json.dump(errortotal, outfile)
        else:
            print("Fail. try harder next time")
            with open('Prevscore.json', 'w') as outfile:
                json.dump(errortotal, outfile)
    return errortotal;

