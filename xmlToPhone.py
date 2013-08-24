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
if not os.path.exists(temporary_music_dir):
    os.makedirs(temporary_music_dir)

print "Creating temporary directory structure..."
for file_loc in url_locs:
    actual_path = path.abspath(music_dir + file_loc).replace('&amp;','&')
    new_song_dir_loc = path.abspath(temporary_music_dir + file_loc[:file_loc.rfind('/')]).replace('&amp;','&')
    new_song_loc = path.abspath(temporary_music_dir+file_loc).replace('&amp;','&')
    if not path.exists(new_song_dir_loc):
        os.makedirs(new_song_dir_loc)
    if not path.exists(new_song_loc):
        shutil.copy(actual_path, new_song_loc)
"...done"

print "Pushing all files..."
call(["adb","push", temporary_music_dir,"/sdcard/Music"])
print "...done"
