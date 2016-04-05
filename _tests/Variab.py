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
# logger = logging.getLogger('spellcheck')
pwl = enchant.request_pwl_dict("Dict.txt")
# add words to the dictionary used to test for spelling errors
spellcheck = SpellChecker("en_GB", filters=[URLFilter, EmailFilter])
filenameslist = glob.glob("./_posts/*.md")
# loads files
wordswrong = open("WordsWrong.txt", "w+")
# creates new file to save the words that were spelt wrong
filecheck = open("FileCheck.txt", "w+")
# creates new file to save which file it checked
