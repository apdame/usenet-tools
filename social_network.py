'''
Culls emails using key terms from archives for social network analysis.
Uses sets to track which messages have already been collected.
'''

import csv
import mailbox
import email
import dateutil.parser
import glob, os

'''
Uncomment word_list and use if you're collecting messages
based on specific content.

word_list =[]
'''

#seen contains messages already made into nodes
#refnodes contains messages that are referenced by nodes,
#but node info and references need to be collected
seen = set()
refnodes = set()
    
def msgindex(message, payload):
    #indexes information for nodes
    global address
    global sender
    global year
    global reply
    global ngs
    global term

    address = str(message.get("Message-ID")).replace("#1/1", "")
 
    sender = str(message.get("From")).strip()
    if message.has_key('References') is True:
        reply = "Reply"
    else:
        reply = "Original"

    dt = message['Date']
    dt = dateutil.parser.parse(message['Date'])
    year = dt.year

    ngs = str(message['Newsgroups']).replace(",", " | ")

    if any(word in payload for word in word_list):
        term = "Appears"
    else:
        term = "Absent"
    
    return address, sender, year, reply, ngs

def replies(message):
    #collects message replies to make edges
    global refs
    
    refs = str(message.get("References"))
    refs = refs.strip(" ")
    
    if "><" or "> <" in refs:
        #cleans up < and > around Message IDs
        refs = ''.join(refs.split())
        refs = refs.replace("><", ">,<").split(',')
        for i in refs:
            i = i.strip("<").strip(">")
            i = "<" + i + ">"
    else:
        return refs
    
    return refs

'''
If you are collecting messages with specific
content you'd like to analyze, uncomment this function

def messages(message, mid, payload, msgfile):
    #writes content of all messages collected to .txt file
    msgseen = set()
    msg = message.as_string()
    if mid in msgseen:
        pass
    else:
        if any(word in payload for word in word_list):
            msgfile.write("From %s\n%s\n" % (str(message["From"]), msg))
            msgseen.add(mid)
        else:
            pass
'''

def nodes(message, mid, payload, csv_file1, writer1):
    #Writes node information to csv file
    if mid in seen:
        pass
    '''
    Again, for use when searching for specific content.
    
    elif any(word in payload for word in word_list):
        msgindex(message, payload)
        writer1.writerow([address] + [sender] + [reply] + [year] + [ngs] + [term])
        seen.add(mid)
    '''
    elif mid not in seen and mid in refnodes:
        msgindex(message, payload)
        writer1.writerow([address] + [sender] + [reply] + [year] + [ngs])
        seen.add(mid)
    else:
        pass

            
def edges(message, mid, csv_file2, writer2):
    #list of edges collected
    edgesseen = set()
    if mid in seen:
        #checks if node info exists. If so, checks if msg has references
        #and they haven't been collected yet.
        if mid not in edgesseen and message.has_key('References') is True:
            replies(message)
            #adds msg to edges collected
            edgesseen.add(mid)
            for i in refs:
                refnodes.add(i)
                #add refs to set to be checked later in noderefs()
                writer2.writerow([mid] + [i])
        else:
            pass
    else:
        pass



def noderefs(message, mid, csv_file1, writer1, csv_file2, writer2):
    #checks if references in refnodes are in seen
    #so already collected. If not, collects node info
    #and edges, then removes them from set refnodes.
    if mid in refnodes and mid not in seen:
        nodes(message, mid, csv_file1, writer1)
        edges(message, mid, csv_file2, writer2)
        refnodes.remove(mid)
    else:
        pass

def main():
    global csv_file1
    global csv_file2
    global writer1
    global writer2

    prefix = raw_input("How should the files be prefixed? ")
    with open('%sMessages.txt' % prefix, 'w') as msgfile, open('%s_Nodes.csv' % prefix, 'wb+') as csv_file1, open('%s_Edges.csv' % prefix, 'wb+') as csv_file2:          
        writer1 = csv.writer(csv_file1, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar=' ', skipinitialspace=False, escapechar='\\')
        writer2 = csv.writer(csv_file2, delimiter=',', quoting=csv.QUOTE_MINIMAL, quotechar=' ', skipinitialspace=False, escapechar='\\')
        writer1.writerow(["Id"] + ["Sender"] + ["Threaded"] + ["Year Posted"] + ["Newsgroups Posted To"])
        writer2.writerow(["Source"] + ["Target"])
        for file in glob.glob("*.mbox"):
            mbox = mailbox.mbox(file)
            print "Reading %s..." % file
            for message in mbox:
                mid = str(message["Message-ID"]).replace("#1/1", "").strip()
                payload = str(message.get_payload())
                #messages(message, mid, payload, msgfile)
                nodes(message, mid, payload, csv_file1, writer1)
                edges(message, mid, csv_file2, writer2)
                noderefs(message, mid, csv_file1, writer1, csv_file2, writer2)
        
        
if __name__=="__main__":
   main()
