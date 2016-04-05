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


def Filechecker():
    if os.listdir('.') == []:
        print('Please put Prevscore.json in the location of this file.')
        end
    if os.listdir('../_posts/') == []:
        print ('No .md files to evaluate')
        end


def linechecker(errortotalprev):
    errortotal = 0
    for filename in filenameslist:
        print('now checking file ', filename)
        error = 0
        icodeblock = False
        # sets not a code block
        linelist = codecs.open(filename, 'r', encoding='UTF-8').readlines()
        for line in linelist:
            skipline = False
            # ##defaults to not skip line
            if line.startswith('```') or line == '---':
                icodeblock = not icodeblock
                if not icodeblock:
                    skipline = True
                    # if detected as codeblock it skips lines
            elif line.startswith('    '):
                skipline = True
                # if detected as a line with code
            if not icodeblock and not skipline:
                htmlnote = re.sub(r'<-(.*)->', 'test', line)
                #print(htmlnote)
                #htmlnotere = htmlnote.match(line).group(1)
                htmlsnip = re.sub(r'\<.*?\>', '', line)
                # strips code between < >
                htmlsnipper = re.sub(r'\`.*?\`', '', htmlsnip)
                chkr12.set_text(htmlnote)
                # strips code between ` `
                chkr.set_text(htmlsnipper)
                # sets text to check to stripped line
                for err in chkr:
                    if pwl.check(err.word):
                        check1 = 1
                        # Filler so it dosent spit out an error
                    else:
                        errortotal = errortotal+1
                        error = error+1
                        wordswrong.write(err.word)
                        wordswrong.write(' in ')
                        wordswrong.write(filename)
                        print('Failed word: ', err.word)
                        wordswrong.write('\n')
                        # writes word and filename to file if spelt wrong
                for err in chkr12:
                    if pwl.check(err.word):
                        check12 = 1
                        # # Filler so it dosent spit out an error
                    else:
                        errortotal = errortotal+1
                        error = error+1
                        wordswrong.write(err.word)
                        wordswrong.write(' in ')
                        wordswrong.write(filename)
                        print('Failed word: ', err.word)
                        wordswrong.write('\n')
                        # writes word + filename to file if word is spelt wrong
                        # file error even though it is copy pasted
        print(error, ' errors in total in ', filename)
        # after it finishes the file it prints out the errors in that file
        filecheck.write('%d errors in total in %s\n' % (error, filename))
        # prints the same line as above in a text document
    print ('Errors in total: ', errortotal)
    # prints errors for all the files
    if errortotal <= errortotalprev:
        print('Pass. you scored better or equal to the last check')
        with open('Prevscore.json', 'w') as outfile:
            json.dump(errortotal, outfile)
            # saves errortotal to json file for future use
    elif errortotal > errortotalprev:
        print('Fail. try harder next time')
        with open('Prevscore.json', 'w') as outfile:
            # saves errortotal to json file for future use
            json.dump(errortotal, outfile)
