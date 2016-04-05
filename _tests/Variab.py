import glob
import os
import enchant
import codecs
import logging
import json
import os.path
import shutil
import re
from enchant.checker import SpellChecker
from enchant.tokenize import EmailFilter, URLFilter
DIRECTORY_TESTS = os.path.dirname(os.path.realpath(__file__))
DIRECTORY_POSTS = os.path.join(DIRECTORY_TESTS, '../_posts/')
JSONSCORE = os.path.join(DIRECTORY_TESTS, 'Prevscore.json')
# logger = logging.getLogger('spellcheck')
pwl = enchant.request_pwl_dict(os.path.join(DIRECTORY_TESTS, 'Dict.txt'))
# add words to the dictionary used to test for spelling errors
spellcheck = SpellChecker("en_GB", filters=[URLFilter, EmailFilter])
chkr12 = SpellChecker("en_GB", filters=[URLFilter, EmailFilter])
filenameslist = glob.glob(os.path.join(DIRECTORY_POSTS,"*.md"))
# loads files
wordswrong = open("WordsWrong.txt", "w+")
# creates new file to save the words that were spelt wrong
filecheck = open("FileCheck.txt", "w+")
# creates new file to save which file it checked
