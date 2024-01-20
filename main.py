import sqlite3

# creates the database with the name "gta.db" if not created already
connection = sqlite3.connect("gta.db")
# the cursor is used for manipulating the database
cursor = connection.cursor()
# executes commands witin the parenthesis
            # (create table name (value        type   , value        type, value type))
try:
    cursor.execute("create table gta (release_year integer, release_name text, city text)")
except:
    print("database already created")

# list used for the project (date released, title name, location)
release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]    

cursor.executemany("insert into gta values (?,?,?)", release_list)
connection.commit()

# opens the database since it has already been created
connection = sqlite3.connect("gta.db")
#prints database rows
print("--------------------------")
cursor.execute("select * from gta where city=:c", {"c", "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)
connection.close()