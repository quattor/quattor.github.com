import glob, os, enchant, codecs, logging, json, os.path, shutil, re
from Variab import *
from Funct import *
errortotalprev = 0
Filechecker();
if os.path.exists("Prevscore.json"):
    with open('Prevscore.json', 'r') as f:
        errortotalprev = json.load(f) #loads json file with errortotalprev in
linechecker(errortotalprev);
filecheck.close() #closes both files that were opened to save contents
wordswrong.close()
