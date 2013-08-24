import sys
import re
from subprocess import call
import os
from os import path
import shutil

xml_file = sys.argv[1]
print "XML File is " + xml_file

music_dir = '/home/mike/Music'
url_locs = []
with open (xml_file, 'r') as read_file:
    for line in read_file:
        search = re.search('<location>file://'+music_dir+'(.*)</location>', line)
        if search is not None:
            url_locs.append(search.group(1))

temporary_music_dir = path.abspath('.tmpmusic')
if os.path.exists(temporary_music_dir):
    shutil.rmtree(temporary_music_dir)
os.makedirs(temporary_music_dir)

print "Creating temporary directory structure..."
for file_loc in url_locs:
    new_song_dir_loc = path.abspath(temporary_music_dir + file_loc[:file_loc.rfind('/')]).replace('&amp;','&')
    if not path.exists(new_song_dir_loc):
        os.makedirs(new_song_dir_loc)
"...done"

new_song_loc = path.abspath(temporary_music_dir+file_loc).replace('&amp;','&')

print "Pushing directory structure..."
call(["adb","push", temporary_music_dir,"/sdcard/Music"])
print "...done"

number_to_copy = len(url_locs)
print "Copying " + str(number_to_copy) + " files"
for idx, file_loc in enumerate(url_locs):
    print "(" + str(idx+1) + "/" + str(number_to_copy) + ")" + "\t\tPushing " + file_loc + "..."
    call(["adb","push", music_dir+file_loc,"/sdcard/Music"])
