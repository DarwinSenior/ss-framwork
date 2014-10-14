__author__ = 'Kevin Renner'

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

#Searches for the songs that correspond to a tag
#Returns a dictionary with song names as keys and the number of tags the song matches as the values
def getSongs(tags):
    data = getData()
    songList = dict()
    for tag in tags:
        for name in data:
            line = data[name]
            if tag in line:
                if name in songList.keys():
                    songList[name] += 1
                else:
                    songList[name] = 1

    return songList

#Runs the tag search using an array 'tags' of tags
if __name__=="__main__":
    tags = {'Pop', 'Orchestra', 'Loud'}
    print(getSongs(tags))
