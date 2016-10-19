'''
Pulls addresses from .mbox files,
thows them in a list. Outputs list to text
file, then uses text file to build total count
of unique emails.
'''

from sys import argv
import csv
import mailbox
from collections import Counter
import os

address = []
script, box, csvfile = argv                  #box = Usenet archive you're working with, csvfile = name of CSV file results will output to.

mbox = mailbox.mbox(box)

with open('addresslist.txt','w') as w:       #Collects addresses into a list and stores them in a .txt file
    for message in mbox:
        address.append(message['from'])
    for item in address:
        w.writelines(str(item).strip() + "\n")

with open('addresslist.txt','r') as addlist, open(csvfile, 'wb+') as csv_file:           #Writes addresses to CSV file
    ngwriter = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,
                          quotechar=' ', skipinitialspace=False, escapechar='\\')
    text = addlist.readlines()
    duplicates = Counter(text)
    for key, value in duplicates.iteritems():
            ngwriter.writerow([str(key).strip()] + [str(value).strip()])

os.remove('addresslist.txt')                                      #Deletes txt file where addresses are stored.


