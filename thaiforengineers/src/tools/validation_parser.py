import urllib, os
from bs4 import BeautifulSoup
from syllableParser import SyllableParser
class ValidationParser (object):

    url = ""
    page = ""
    soup = ""

    def __init__(self):
        parser = SyllableParser()

    def parse(self):
        print os.getcwd()
        file = open("newfile.txt", "w")
        self.page = urllib.urlopen("/Users/sutee/src/thaiforengineers/src/tools/thaiwords.html")
        self.soup = BeautifulSoup(self.page, 'html.parser')
        print "initialized"
        rows = self.soup.findAll('tr')
        for row in rows:
            print "-----"
            tds = row.findAll('td')
            print str(tds)
            if len(tds)==3:
                definition = tds[2].string
                if definition:
                    tones = tds[1].findAll('span')
                    if len(tones) == 1: # only care about one syllable for now
                        thaiword=tds[0].string
                        print tds[0].findAll('a')[0].string
                        for tone in tones:
                            file.write(thaiword.encode('utf8')+"\t"+definition.encode('utf8')+"\t"+tone.string.encode('utf8')+"\n")
                            print tone.string
                            print definition
        file.close()

def _main():
    print "start parsing"
    p = ValidationParser()
    p.parse()

if __name__ == "__main__":
    _main()