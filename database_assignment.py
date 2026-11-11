

# Import sqlite3 to create and manage a database
import sqlite3


# List of filenames provided in the assignment
fileList = ('information.docx' , 'Hello.txt' , 'myImage.png' ,
            'myMovie.mpg' , 'World.txt' , 'data.pdf' , 'myPhoto.jpg')


# Connect to the SQLite database
conn = sqlite3.connect('files.db')


# Creating a table with an ID and filename
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename TEXT)")



# Loop through each filename in the list
    for file in fileList:

        # Only select the files ending with .txt
        if file.endswith('.txt'):

            #Insert the qualifying filename into the database
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files (col_filename) VALUES (?)", (file,))



# Retrieve filenames from the database
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_filename FROM tbl_files")
    rows = cur.fetchall()

    # Print each qualifying filename
    for row in rows:
        print(row[0])



# Closing the database connection
conn.close()
        
                
    
