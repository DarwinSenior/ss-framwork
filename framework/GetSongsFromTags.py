__author__ = 'Kevin Renner & HKJ'

import re
import operator
import os
from collections import OrderedDict
#import songtags.dbinteract


#Gets tag data from a CSV file
#Returns dictionary with song names as keys and tags as values
def get_data():
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
#    return songtags.dbinteract.get_songs_and_tags_dict()

#Returns dict containing the scores for tag comparisons
def get_score_data():
    scoreData = dict()
    pwd = os.path.dirname(__file__)
    file = open(os.path.join(pwd, "tagscore.csv"))
    lines = file.readlines()
    databaseTags = lines[0].strip().split(",")
    comparingTags = list()
    for l in lines:
        comparingTag = l.strip().split(",")[0]
        comparingTags.append(comparingTag)
    i = 0
    for databaseTag in databaseTags:
        j = 0
        for comparingTag in comparingTags:
            if lines[i].strip().split(",")[j].isdigit():
                scoreData[(databaseTag, comparingTag)] = int(lines[i].strip().split(",")[j])
            else:
                scoreData[(databaseTag, comparingTag)] = 0
            j += 1
        i += 1
    return scoreData

#Returns the result of a tag comparison
def compare_tags(databaseTag, comparingTag):
    scoreData = get_score_data()
    score = scoreData[(databaseTag, comparingTag)]
    return score

#Searches for the songs that correspond to a tag
#Returns an OrderedDict with song names as keys and tag match scores as the values
def get_songs(tags):
    data = get_data() # You can also use getDBData() now to pull from the database
    songList = dict()
    for comparingTag in tags:
        for name in data:
            line = data[name]
            score = 0
            for databaseTag in line:
                score += compare_tags(databaseTag, comparingTag)
            if name in songList.keys():
                songList[name] += score
            else:
                songList[name] = score
            #if tag in line and name in songList.keys():
            #    songList[name] += 1
            #else:
            #    songList[name] = 1
    newSongList = sort_songs(songList)
    return newSongList

# input: songList dict, containing name keys and score values
# returns: songList OrderedDict, sorted by score order
def sort_songs(songList):
    newSongList = OrderedDict(sorted(songList.iteritems(), key=operator.itemgetter(1), reverse=True))
    return newSongList

def thesaurus(tag):


#Runs the tag search using an array 'tags' of tags
if __name__=="__main__":
    # print "Welcome to song search via tag\n"
    # print "Enter tags seperated by a comma\n"
    # rInput = raw_input()
    # pattern = re.compile("^\s+|\s*,\s*|\s+$")
    # tags = [x.capitalize() for x in pattern.split(rInput) if x]
    # for w in sorted(get_songs(tags), key=get_songs(tags).get, reverse=True):
    #     print w, get_songs(tags)[w]
    print get_songs(["Loud", "Classical"])