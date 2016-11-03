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

address = []
script, box, csvfile = argv
#box = Usenet archive you're working with
#csvfile = name of CSV file results will output to.

with open(box,'r') as addlist, open(csvfile, 'wb') as csv_file:           
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,
                          quotechar=' ', skipinitialspace=False, escapechar='\\')
    for message in mbox:
        address.append(str(message['from']).replace("#1/1", ""))
    for item in address:
        item = ''.join(item.split())
    #Identifies unique addresses
    duplicates = Counter(address)
    writer.writerow(["Address"] + ["Count"])
    for key, value in duplicates.iteritems():
        #Writes addresses to CSV file
        writer.writerow([str(key)] + [str(value)])
