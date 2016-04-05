import glob
import os
import enchant
import codecs
import logging
import json
import os.path
import shutil
import re
from Variab import *
# variables saved in this file
from Funct import *
# functions saved in this file
errortotalprev = 0
# here to save python from throwing out an error
Filechecker()
if os.path.exists("Prevscore.json"):
    with open('Prevscore.json', 'r') as f:
        errortotalprev = json.load(f)
        # loads json file with errortotalprev in
linechecker(errortotalprev)
filecheck.close()
# closes both files that were opened to save contents
wordswrong.close()
