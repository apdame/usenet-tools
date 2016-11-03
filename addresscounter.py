'''
Pulls addresses from .mbox files,
thows them in a list. Outputs list to text
file, then uses text file to build total count
of unique emails.
'''

import csv
import mailbox
import email.message
from collections import Counter

address = []

mbox = mailbox.mbox(raw_input("What is the mailbox you want to work with? "))
print "Reading File..."

for message in mbox:
    msg = str(message["From"])
    address.append(msg)
for item in address:
    item = ''.join(item.split())

csvf = raw_input("What is the name of the csv file it should output to? ")
print "Writing To File..."

with open(csvf, 'wb') as csv_file:           
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL,
                          quotechar=' ', skipinitialspace=False, escapechar='\\')
    #Identifies unique addresses
    duplicates = Counter(address)
    writer.writerow(["Address"] + ["Count"])
    for key, value in duplicates.iteritems():
        #Writes addresses to CSV file
        writer.writerow([str(key)] + [str(value)])
