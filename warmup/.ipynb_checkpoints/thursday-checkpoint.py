#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('challenge.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE IF NOT EXISTS THURSDAY
 (ID INT PRIMARY KEY     NOT NULL,
 BAND           TEXT    NOT NULL,
 HOMETOWN       TEXT     NOT NULL,
 YEAR           INT      NOT NULL);''')
print("Table created successfully")


conn.execute("INSERT INTO THURSDAY (ID,BAND,HOMETOWN,YEAR) VALUES (1, 'The Beatles', 'Liverpool, England', 1960)")

conn.execute("INSERT INTO THURSDAY (ID,BAND,HOMETOWN,YEAR) VALUES (2, 'Guns and Roses', 'Los Angeles, USA', 1985)")

conn.execute("INSERT INTO THURSDAY (ID,BAND,HOMETOWN,YEAR) VALUES (3, 'Agnee', 'Pune, India', 2007)")

conn.commit()
print("Records created successfully")


#!/usr/bin/env python3

cursor = conn.execute("SELECT id, band, hometown, year from THURSDAY")
for row in cursor:
    print("ID = ", row[0])
    print("BAND = ", row[1])
    print("HOMETOWN = ", row[2])
    print("YEAR = ", row[3], "\n")

print("Operation done successfully")
conn.close()


