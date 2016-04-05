import glob
import os
import enchant
import os.path
from enchant.checker import SpellChecker
from enchant.tokenize import EmailFilter, URLFilter
import sys

DIRECTORY_TESTS = os.path.dirname(os.path.realpath(__file__))
DIRECTORY_ROOT = os.path.dirname(DIRECTORY_TESTS)
DIRECTORY_POSTS = os.path.join(DIRECTORY_ROOT, '_posts')

JSONSCORE = os.path.join(DIRECTORY_TESTS, 'Prevscore.json')
FILENAME_PWL = os.path.join(DIRECTORY_TESTS, 'Dict.txt')

print("Location of root directory is '%s'" % DIRECTORY_ROOT)
print("Location of tests directory is '%s'" % DIRECTORY_TESTS)
print("Location of posts directory is '%s'" % DIRECTORY_POSTS)
print("Location of json score file is '%s'" % JSONSCORE)

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
wordswrong = open("WordsWrong.txt", "w+")
# creates new file to save the words that were spelt wrong
filecheck = open("FileCheck.txt", "w+")
# creates new file to save which file it checked
