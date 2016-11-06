'''
Workaround for issue with Python mailbox module mis-reading Usenet
Historical Collection mbox files. Identifies all instances of "from"
that are *not* in the header, changes them to "xFrom," and writes
them to a new mailbox.
'''

batch = []

box = raw_input("What is the mailbox you want to work with? ")
newbox = raw_input("What is the name of the file it should output to? ")

with open(box, 'rb') as original, open(newbox, 'wb') as new:
    for line in original:
        if "From " in line:
            num = line[6]
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

print "Editing complete!"
