import glob, os, enchant, codecs, logging, json, os.path, shutil, re
from Variab import *
from Funct import *
errortotalprev = 0
if os.path.exists("Prevscore.json"):
    with open('Prevscore.json', 'r') as f:
        errortotalprev = json.load(f)
Filechecker();
linechecker(errortotalprev);
filecheck.close()
wordswrong.close()

