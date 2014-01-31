# -*- coding: utf-8 -*-

import re
import csv
import os
import calendar
from datetime import date

def __parse_beers__(beers, location, list_type):
    apostrophe_regex = re.compile(r"’", re.MULTILINE)    
    correction_regex = re.compile(r"(ipa|usa)", re.MULTILINE | re.IGNORECASE)
    
    num_regex = re.compile(r"^(\d+)\.?\s?", re.MULTILINE)          
    line_regex = re.compile(r"\b(\d{2,3}.*$)", re.MULTILINE)        
    glass_regex = re.compile(r"(?<=\t)([ ]*glass -\s*)|([ ]*1/2 Liter -\s*)(?=\$)", re.MULTILINE | re.IGNORECASE) 
    amount_regex = re.compile(r"(\$\d{1,2}\.\d{2}).*", re.MULTILINE)
    
    abv_regex = None
    if list_type.lower() == "draft":
        abv_regex = re.compile(r"\s+(\d+(\.\d{1,2})?)%", re.MULTILINE)
    else:
        abv_regex = re.compile(r"\s+(\d+(\.\d{1,2})?)%?", re.MULTILINE)            
    
    beers = apostrophe_regex.sub(r"'", beers)    
    beers = correction_regex.sub(lambda x: x.group(1).upper(), beers)
    
    matches = line_regex.findall(beers)
    
    for match in matches:
        match = num_regex.sub(r"\1\t\t\t", match)
        match = abv_regex.sub(r"\t\t\t\1\t", match)
        match = glass_regex.sub(r"", match)
        match = amount_regex.sub(r"\t\1\t", match, 1)
        match += "%s\t%s" % (list_type, location)
        print match
        yield match

def parse_draft_list(draft_string, location):
    beers = __parse_beers__(draft_string, location, "Draft")
    output_csv(beers, location)
    print_beers(beers)

def parse_exclusives_list(draft_string, location):    
    beers = __parse_beers__(draft_string, location, "Exclusive")
    output_csv(beers, location)
    print_beers(beers)
def parse_seasonal_list(draft_string, location):    
    beers = __parse_beers__(draft_string, location, "Seasonal")
    output_csv(beers, location)
    print_beers(beers)
        
def print_beers(beers):
    for line in beers:
        print line

def output_csv(beer_list, location):
    columns = [
        "TourNumber",
        "Brewey",
        "Name",
        "DisplayName",
        "Style",
        "Country",
        "ABV",
        "Size",
        "Price",
        "BeerType",
        "Location"
    ]
    
    file_name = "wlplacemat_%s.csv" % (calendar.month_name[date.today().month].lower()) 
    file_path = r"C:\Users\ivalverde\Desktop\%s" % (file_name)
    mode = "wb"
    
    if os.path.exists(file_path):
        mode = "ab"
    try:    
        with open(file_path, mode) as beer_csv:
            wr = csv.writer(beer_csv, csv.QUOTE_ALL)            
            if mode != "ab":
                wr.writerow(columns)                
            for line in beer_list:
                wr.writerow(line.split("\t"))
    except IOError as e:
        print "IOError in output_csv: %s" % (e.message)