'''
Workaround for issue with Python mailbox module mis-reading Usenet
Historical Collection mbox files. Identifies all instances of "from"
that are *not* in the header, changes them to "xFrom," and writes
them to a new mailbox.
'''
from sys import argv

batch = []
script, box, newbox = argv
#box = current mailbox file
#newbox = new file. Can be .mbox, but doesn't have to be.

with open(box, 'rb') as original, open(newbox, 'wb') as new:
    for line in original:
        if "From " in line:
            num = line[-2]
            #Checks to see if is added Google Groups header
            if num.isdigit() is True:
                #Skips edit if True
                batch.append(line)
            else:
                x = line.replace("From ", "xFrom ")
                batch.append(x)
        else:
            batch.append(line)
    for line in batch:
        #Writes edited mailbox to new file
        new.writelines(line)
