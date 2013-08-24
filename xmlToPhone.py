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

number_to_copy = len(url_locs)
for idx, file_loc in enumerate(url_locs):
    print "(" + str(idx) + "/" + str(number_to_copy) + ")" + "\t\tPushing " + file_loc + "..."
    call(["adb","push", file_loc,"/sdcard/Music"])
