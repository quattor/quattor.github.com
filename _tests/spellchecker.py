import glob
import os
import enchant
import os.path
import configparser
import json
from enchant.checker import SpellChecker
from enchant.tokenize import EmailFilter, URLFilter
import sys
from funct import filechecker
from funct import linechecker
DIRECTORY_TESTS = os.path.dirname(os.path.realpath(__file__))
CONFIGFILE = configparser.ConfigParser()
CONFIGFILECOMPLETEPATH = os.path.join(DIRECTORY_TESTS, 'config.ini')
CONFIGFILE.read(CONFIGFILECOMPLETEPATH)
CONFIGFILE.read(DIRECTORY_TESTS, 'config.ini')
DEFAULTCONFIGFILE = CONFIGFILE['DEFAULT']
DIRECTORY_ROOT = os.path.dirname(DIRECTORY_TESTS)
DIRECTORY_POSTS = os.path.join(DIRECTORY_ROOT, DEFAULTCONFIGFILE['Filestocheckdir'])
FILENAME_JSONSCORE = DEFAULTCONFIGFILE['Prevscore']
FILENAME_PWL = DEFAULTCONFIGFILE['PWL']
if not os.path.isabs(FILENAME_JSONSCORE):
    FILENAME_JSONSCORE = os.path.join(DIRECTORY_TESTS, DEFAULTCONFIGFILE['Prevscore'])
if not os.path.isabs(FILENAME_PWL):
    FILENAME_PWL = os.path.join(DIRECTORY_TESTS, DEFAULTCONFIGFILE['PWL'])


print(DIRECTORY_POSTS)
#print("Location of root directory is '%s'" % DIRECTORY_ROOT)
#print("Location of tests directory is '%s'" % DIRECTORY_TESTS)
#print("Location of posts directory is '%s'" % DIRECTORY_POSTS)
#print("Location of json score file is '%s'" % FILENAME_JSONSCORE)

# logger = logging.getLogger('spellcheck')
if os.path.exists(FILENAME_PWL):
    print("PWL file exists")
    pwl = enchant.request_pwl_dict(FILENAME_PWL)
    print("Loaded PWL object: %s" % pwl)
    print("Methods of object: %s" % dir(pwl))

else:
    print("PWL file does not exist")
    sys.exit(2)
# add words to the dictionary used to test for spelling errors
spellcheck = SpellChecker("en_GB", filters=[URLFilter, EmailFilter])
filenameslist = glob.glob(os.path.join(DIRECTORY_POSTS,"*.md"))
# loads files
wordswrong = open(CONFIGFILE['DEFAULT']['Wordswrongfile'], "w+")
# creates/opens a file to save the words that were spelt wrong
filecheck = open(CONFIGFILE['DEFAULT']['Filecheck'], "w+")
# creates/opens a file to save the files that were checked
def main():
    errortotalprev = 0
    filechecker(DIRECTORY_POSTS)
    if os.path.exists(FILENAME_JSONSCORE):
        with open(FILENAME_JSONSCORE, 'r') as f:
            errortotalprev = json.load(f)
    passed = linechecker(errortotalprev, pwl, filenameslist, filecheck, wordswrong, spellcheck, FILENAME_JSONSCORE)
    filecheck.close()
    wordswrong.close()
    if not passed:
        sys.exit(1)

if '__main__' == '__main__':
    main()
