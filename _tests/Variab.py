import glob, os, enchant, codecs, logging, json, os.path, shutil, re
from enchant.checker import SpellChecker
from enchant.tokenize import EmailFilter, URLFilter
#logger = logging.getLogger('spellcheck')
pwl = enchant.request_pwl_dict("./_tests/Dict.txt") #add words to the dictionary used to test for spelling errors
chkr = SpellChecker("en_GB", filters=[URLFilter, EmailFilter])
#chkr1 = SpellChecker("en_GB")
filenameslist = glob.glob("./_posts/*.md") #loads files
pwl = enchant.request_pwl_dict("./tests/Dict.txt")
check1 = 0
wordswrong = open("WordsWrong.txt", "w+") #creates new file to save the words that were spelt wrong
filecheck = open("FileCheck.txt", "w+") #creates new file to save which file it checked
