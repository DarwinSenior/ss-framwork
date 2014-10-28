__author__ = 'Kevin Renner & HKJ'

import re
import operator
import os
#import songtags.dbinteract


#Gets tag data from a CSV file
#Returns dictionary with song names as keys and tags as values
def getData():
    data = dict()
    pwd = os.path.dirname(__file__)  # get current directory
    datafile = open(os.path.join(pwd, "data"))
    lines = datafile.readlines()
    for line in lines:
        songData = line.strip().split(",")[1:]
        name = line.split(",")[0]
        data[name] = songData
    datafile.close()
    return data


#def getDBData():
 #   return songtags.dbinteract.get_songs_and_tags_dict()


def getScoreData():
    scoreData = dict()
    pwd = os.path.dirname(__file__)
    file = open(os.path.join(pwd, "tagscore.csv"))
    line = file.readlines()
    keysX = line[0].strip().split(",")
    keysY = list()
    for l in line:
        keysY.append(l.strip().split(",")[0])
    i = 0 #Incrementing value for following for loop
    for keyX in keysX: #Still trying to get this loop to work, should save the table of values using the column and line headers as a key in a tuple
        j = 0
        for keyY in keysY:
            scoreData[(keyX, keyY)] = line[i].strip().split(",")[j]
            j += 1
        i += 1
    return scoreData


#Searches for the songs that correspond to a tag
#Returns a dictionary with song names as keys and the number of tags the song matches as the values
def getSongs(tags):
    data = getData() # You can also use getDBData() now to pull from the database
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
    #print "Welcome to song search via tag\n"
    #print "Enter tags seperated by a comma\n"
    #rInput = raw_input()
    #pattern = re.compile("^\s+|\s*,\s*|\s+$")
    #tags = [x.capitalize() for x in pattern.split(rInput) if x]
    #for w in sorted(getSongs(tags), key=getSongs(tags).get, reverse=True):
    #    print w, getSongs(tags)[w]
    scoreData = getScoreData()
    print scoreData[("Leonard Berstein", 'Orchestra')]
