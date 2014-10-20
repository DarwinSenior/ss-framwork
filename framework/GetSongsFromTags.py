__author__ = 'Kevin Renner & HKJ'

import re
import operator	

#Gets tag data from a CSV file
#Returns dictionary with song names as keys and tags as values
def getData():
    data = dict()
    file = open("data")
    lines = file.readlines()
    for line in lines:
        songData = line.strip().split(",")[1:]
        name = line.split(",")[0]
        data[name] = songData
    file.close()
    return data

def getScoreData():
    file = open("tagscore.csv")


#Searches for the songs that correspond to a tag
#Returns a dictionary with song names as keys and the number of tags the song matches as the values
def getSongs(tags):
    data = getData()
    songList = dict()
    for tag in tags:
        for name in data:
            compareToTag(songList, data, name, tag)

    return songList

#Adds songs to the songList dict if they match a tag. Each song is initialized with a value of one, and is incremented by one for each tag matched
def compareToTag(songList, data, name, tag):
    line = data[name]
    if tag in line:
        if name in songList.keys():
            songList[name] += 1
        else:
            songList[name] = 1



#Runs the tag search using an array 'tags' of tags
if __name__=="__main__":
    print "Welcome to song search via tag\n"
    print "Enter tags seperated by a comma\n"
    rInput = raw_input()
    pattern = re.compile("^\s+|\s*,\s*|\s+$")
    tags = [x.capitalize() for x in pattern.split(rInput) if x]
    for w in sorted(getSongs(tags), key=getSongs(tags).get, reverse=True):
        print w, getSongs(tags)[w]
