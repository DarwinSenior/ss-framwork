import MySQLdb
__author__ = 'Kevin Renner'

#This code accepts a list of tags as input, and returns a list of songs that fit the tag.
#Eventually it will be able to rank the songs in order of what song fit the most tags

db = MySQLdb.connect("localhost", "root", "password", "test") #MySQL connection information. In the real application this can be moved to another file
cursor = db.cursor()

def getSongsFromTags(tags):
    songList=[]
    newSongList = []
    for tag in tags:
        sql = "SELECT * FROM '%s'"; "%(tag)"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            songList.append(results[row])
    for songA in songList:
        repeat = 0
        for songB in songList:
            if songA == songB:
                repeat += 1
        if repeat <= 1:
            newSongList.append(songA)
    return newSongList



