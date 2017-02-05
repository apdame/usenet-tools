# usenet-tools
Included in this repo are a variety of short, simple scripts I've written for doing data mining and analysis on the files held in [the Usenet Historical Collection from the Internet Archive](https://archive.org/details/usenethistorical). All scripts are written in Python 2.7. I've included short descriptions of each module below, to give an idea of their functions and any existing bugs. 

I'll be adding more scripts as I successfuly write/debug them. I've focused on making the scripts fairly simple and able to run entirely through the command line, so you don't need non-standard libraries (except [dateutil](https://dateutil.readthedocs.io/en/stable/)) or a deep knowledge of Python to use them. When inputting file names in the command line, make sure you include the file extension at the end (IE: .csv, .txt, .mbox).

* fromedit.py - *Before you use any of these other modules, you'll want to run this one.* Workaround for issue with Python mailbox module mis-reading Usenet Historical Collection mbox files, which I discuss in detail [here](http://mith.umd.edu/listening-for-the-static/). Identifies all instances of "from" that are *not* in the header, changes them to "xFrom," and writes them to a new file. Otherwise, message will falsely detect any instance of "\nFrom " as the start of a new message.

* msgprinter.py - Prints out each message from a Usenet Collection into individual .txt files, labeled via prefix + number. This may make Usenet collections easier to work with in analysis programs like NVivo (since you can isolate single messages). As part of this process, this script reverts the changes made by fromedit.py.

* addresscounter.py - Collects poster addresses from the given newsgroup archive and counts number of occurrances in the archive. You may want to run the .csv through a plain text editor to remove all the whitespace after you have your output - because .mbox data comes out NoneType, .join() and .strip() doesn't always work as they should. I'm still working on a solution for this.

* crosspost.py - Culls the unique Message IDs and Newsgroup listings for the given newsgroup archive, alphabetizes newsgroup list, then stores them in a dictionary. Dictionary inputs to .csv for analysis. To get the lists as they appear in the archive, comment out (#) the sorted() and .join() lines.

* cisgender_network.py - The code used to build the Cisgender Usage Network. I talk a bit more about building the network, and the limitations of using social network analysis on Usenet [here](http://mith.umd.edu/visualizing-poster-activity-usenet/).

* social_network.py - A generic version of the cisgender network script for social network analysis of Usenet collections. This one will work with any Usenet collection, as long as it's in the same directory as the Usenet collection files. It's set to search for .mbox, but you can easily switch that out for another extension. Note that I've commented out all portions that search for specific terms, but these can be uncommented and terms added to word_list if you're looking for specific usage patterns.
