import sys
import re
from subprocess import call

xml_file = sys.argv[1]
print "XML File is " + xml_file

url_locs = []
with open (xml_file, 'r') as read_file:
    for line in read_file:
        search = re.search('<location>file://(.*)</location>', line)
        if search is not None:
            url_locs.append(search.group(1))

for i in url_locs:
    print "Pushing " + i + "..."
    call(["adb","push",i,"/sdcard/Music"])
