'''
Culls the unique IDs and Newsgroup listings for
newsgroup, stores them in a dictionary,
then inputs to .csv for analysis.
'''

import mailbox
import csv

crosspost = {}

mbox = mailbox.mbox(raw_input("What is the mailbox you want to work with? "))
csvf = raw_input("What is the name of the csv file it should output to? ")

print "Reading File..."

for message in mbox:
    msg = str(message['Message-ID']).replace("#1/1", "").strip()
    msg += ","
    #collects Message-ID and cleans it up a bit
    ng = str(message['Newsgroups']).split(',')
    #Alphabetizes list for uniformity. You can omit the
    #next two lines if you want to get the lists "as is."
    ngs = sorted(ng)
    ng = ','.join(ngs)
    #Sets ID as key, with Alpha Newsgroups as value
    crosspost[msg] = ng

print "Writing To File..."

with open(csvf, 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Message ID"] + ["Newsgroups"])
    for key, value in crosspost.iteritems():
        #writes row with Message ID and
        #list of Newsgroups, 1 newsgroup per cell
        writer.writerow([key] + [value])

print "Writing Complete!"
