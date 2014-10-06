__author__ = 'Kevin Renner'
import MySQLdb

db = MySQLdb.connect("localhost", "root", "password",
                     "test")  # This connects to the database
cursor = db.cursor()  # Cursor object, I think this is used for executing the command in the database

# Insert code here for gathering user input, and then interacting with the database
operation = raw_input("Choose an operation: 'Add' or 'View'")
if operation == 'Add':  # Code for adding songs and data to database
    name = raw_input("Song Name:")
    artist = raw_input("Artist:")
    album = raw_input("Album:")
    genre = raw_input("Genre:")
    year = raw_input("Year:")
    tags = raw_input("Tags:")

    sql = "INSERT INTO Songs(Name, Artist, Genre, Year, Tags, Album) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');"%(name, artist, genre, year, tags, album)
    print(sql)
    try:
        cursor.execute(sql)  #Executes sql
        db.commit()  #Finalizes changes in db
        print "Song " + name + " Added"

    except:
        db.rollback()  # If there is an error, changes are not made
        print "Input failed"
        print cursor


elif operation == 'View':  # Code for viewing data in database
    print "This operation is not yet functional"

db.close()

#One other note: In the real program, we will need to sanitize inputs (see http://xkcd.com/327/ for reference)