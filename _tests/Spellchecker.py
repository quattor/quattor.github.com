import glob, os, enchant, codecs, logging, json, os.path, shutil
from enchant.checker import SpellChecker
logger = logging.getLogger('spellcheck')
pwl = enchant.request_pwl_dict("Dict.txt")
chkr = SpellChecker("en_GB")
filenameslist = glob.glob("../_posts/*.md")
pwl = enchant.request_pwl_dict("Dict.txt")
errortotal=0
wordswrong = open("WordsWrong.txt", "w+")
filecheck = open("FileCheck.txt", "w+")
if os.path.exists("Prevscore.json"):
    with open('Prevscore.json', 'r') as f:
        data = json.load(f)
else:
    print("Please put Prevscore.json in the location of this file.")
if os.listdir("../_posts/") == []:
    print ("No .md files to evaluate")
else:
    for filename in filenameslist:
        print("now checking file ", filename)
        error=0
        icodeblock = False
        linelist = codecs.open(filename,'r', encoding='UTF-8').readlines()
        for line in linelist:
            skipline = False
            if line.startswith("```") or line == "---":
                icodeblock = not icodeblock
                if not icodeblock:
                    skipline = True
            elif line.startswith("    "):
                skipline = True
            if not icodeblock and not skipline:
                
                chkr.set_text(line)
                for err in chkr:
                    if pwl.check(err.word):
                        test = 1
                        #logger.info("Word found in personal word list: %s", err.word)
                    else:
                        error=error+1
                        errortotal=errortotal+1
                        wordswrong.write(err.word)
                        wordswrong.write(" in ")
                        wordswrong.write(filename)
                        print("Failed word: ", err.word)
                        wordswrong.write("\n")
        print(error," errors in total in ", filename)
        filecheck.write("%d errors in total in %s\n" % (error, filename))
print(errortotal," errors in total.")
if errortotal <= data:
    print("Pass. you scored better or equal to the last time")
if errortotal > data:
    print("Fail. try harder next time")
filecheck.close()
wordswrong.close()
with open('Prevscore.json', 'w') as f:
     json.dump(errortotal, f)
input()

