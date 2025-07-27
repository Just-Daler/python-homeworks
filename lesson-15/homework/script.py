import sqlite3
"""1- Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
The Name and Species columns should be text fields, and the Age column should be an integer field."""


creat_table = ("""create table  IF NOT EXISTS Roster(
                Name text,
                Species text,
                Age integer
                )
                """)
with sqlite3.connect("Roster.db") as c:
    ed =c.cursor()
    ed.execute(creat_table)
    result = ed.execute("Select * from Roster")
print(result.fetchall())

"""2-Populate your new table with the following values:"""

values = (("Benjamin Sisko","Human",40),
          ("Jadzia Dax","Trill",300),
          ("Kira Nerys","Bajoran",29))
          

with sqlite3.connect("Roster.db") as c:
    ed =c.cursor()
    ed.executemany("insert into Roster values(?,?,?)",values)
    result = ed.execute("Select * from Roster")
print(result.fetchall())



"""3-Update the Name of Jadzia Dax to be Ezri Dax"""
with sqlite3.connect("Roster.db") as c:
    ed =c.cursor()
    ed.execute("Update Roster set  name =? where Species = ? and Age = ?",("Ezri Dax","Trill",300))
    result = ed.execute("Select * from Roster")
print(result.fetchall())

"""Display the Name and Age of everyone in the table classified as Bajoran."""

fil_ter = """Select * from Roster
                where species like "Bajoran"
                """


filter = sqlite3.connect("Roster.db")
result = filter.execute(fil_ter)
print(result.fetchall())


