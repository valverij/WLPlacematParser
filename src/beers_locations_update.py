# -*- coding: utf-8 -*-

import sqlite3
import csv
import re

with open(r"C:\Users\ivalverde\Desktop\wlplacemat_january.csv") as beer_csv:    
    reader = csv.reader(beer_csv)
    
    # define variables for loop below
    i = 0
    columns = ""
    num_headers = 0
    location_index = None
    tour_index = None
    
    # navigate csv file
    for row in reader:
        # first row contains header information
        if i == 0:
            # set index of columns for data inserts/updates
            tour_index = row.index("TourNumber")
            location_index = row.index("Location")
            
            # pop the location column so it matches the table schema and doesn't mess up the parameter counts
            row.pop(location_index)
            
            # nab the parameter count and create the column list for INSERT statements
            num_headers = len(row)
            columns = ",".join(row)           
        else:
            # pop the location column and grab the value for the relationship insert
            location = row.pop(location_index)
            
            # open our connection            
            with sqlite3.connect(r"test.sqlite") as conn:
                db = conn.cursor()
                beerID = None
                locationID = None
                
                # spruce up the parameters
                params = [re.sub("\$(.*)", r"\1", col.strip()) or None for col in row]
                
                # insert new rows                
                beer_row = db.execute(r"SELECT * FROM Beers WHERE TourNumber = ?;", [params[tour_index]]).fetchone()
                if beer_row is None:          
                    sql = "INSERT INTO Beers (%s) VALUES (%s);" % (columns, ",".join("?" * num_headers))                          
                    beer_row = db.execute(sql, params)
                    beerID = beer_row.lastrowid
                else:
                    beerID = beer_row[0]
                
                # insert beer/locations relationship
                db.execute(r"INSERT INTO Beers_Locations (BeerID, LocationID) VALUES (?, (SELECT ID FROM Locations WHERE Name = ?));", [beerID, location])
        
        # iterate counter        
        i += 1