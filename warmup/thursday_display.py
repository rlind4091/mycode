#!/usr/bin/env python3                                                                                                           
                                                                                                                                                                                                                                                                    
import sqlite3
conn = sqlite3.connect('challenge.db')
print("Opened database successfully")

cursor = conn.execute("SELECT * from THURSDAY")                                                                                  
for row in cursor:                                                                                                               
    print("ID = ", row[0])
    print("BAND = ", row[1])
    print("HOMETOWN = ", row[2])
    print("YEAR = ", row[3], "\n")

print("Operation done successfully")
conn.close()        
