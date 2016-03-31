import glob, os, enchant, codecs, logging, json, os.path, shutil, re
from enchant.checker import SpellChecker
logger = logging.getLogger('spellcheck')
pwl = enchant.request_pwl_dict("Dict.txt")
chkr = SpellChecker("en_GB")
chkrnote = SpellChecker("en_GB")
filenameslist = glob.glob("../_posts/*.md")
pwl = enchant.request_pwl_dict("Dict.txt")
check1 = 0
wordswrong = open("WordsWrong.txt", "w+")
filecheck = open("FileCheck.txt", "w+")