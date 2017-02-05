'''
Reads mailbox, prints messages to individal txt files.
'''
import os
import mailbox
import dateutil.parser
import re

replacements = {"xFrom": "From", "xxFrom": "From"}

def multiple_replace(dict, text):
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text) 

def main():
    box = mailbox.mbox(raw_input("What is the mailbox you want to work with?(Please include file extension.) "))
    folder = raw_input("What should the folder be named? ")
    print "Printing files..."
    filenum = 1
    for msg in box:
        date = str(msg['Date'])
        mid = str(msg["Message-ID"]).replace("#1/1", "").strip()
        try:
            dt = dateutil.parser.parse(date, fuzzy=True)
        except:
            continue
        dir_path = "%s/%s/%02i/%02i" % (folder, dt.year, dt.month, dt.day)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        file_path = "%s/%s.txt" % (dir_path, mid)
        with open(file_path, "wb") as f:
            txt = msg.as_string()
            content = multiple_replace(replacements, txt)
            f.write(content)
            filenum += 1

    print "Printing complete! %d files printed." % filenum

if __name__=="__main__":
   main()
