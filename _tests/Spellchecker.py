import os
import json
import os.path
import sys
#directory = (os.path.dirname(os.path.realpath(__file__)))
from Variab import *
# variables saved in this file
from Funct import *
# functions saved in this file
errortotalprev = 0
# here to save python from throwing out an error
Filechecker()

if os.path.exists(JSONSCORE):
    with open(JSONSCORE, 'r') as f:
        errortotalprev = json.load(f)
        # loads json file with errortotalprev in
passed = linechecker(errortotalprev, pwl)
filecheck.close()
# closes both files that were opened to save contents
wordswrong.close()

if not passed:
    sys.exit(1)
