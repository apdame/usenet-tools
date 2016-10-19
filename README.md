# usenet-tools
All scripts are written in Python 2.7. I've included short descriptions of each script below, to give an idea of their functions and any existing bugs. I'll be adding more scripts as I successfuly write/debug them. I've focused on making the scripts fairly simple and able to run entirely through the command line, so one doesn't need a deep knowledge of Python to use them.

* addresscounter.py - Collects poster addresses from the file and counts the number of occurrances in the archive. I suggest running the .csv through a plain text editor to remove all the whitespace after you have your oputput - because .mbox data comes out NoneType, .strip() doesn't always work as it should. I'm still working on a solution for this.


