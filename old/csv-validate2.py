#!usr/bin/env python3

import csv

def name():
    pass

def load_data():
#   f = input("Enter filename: ")
    f = 'kap.csv'
    d = csv.DictReader(open(f, 'r'))
    c = d.fieldnames
    return [row for row in d], c
   
    
def display_data(myData, columns, longest):    
    headings = ["| NUM. | "]
    
    for c in columns:
        basewidth = len(c)
        if longest[c] >= 10:
            maxwidth = 10
        else:
            maxwidth = longest[c]
        padding = maxwidth - basewidth
        if padding >= 0:
            headings.extend(c)
            headings.extend(" " * padding)
        else:
            headings.extend(c[0:10])
        headings.extend(" | ")
    headerrow = "".join(headings).rstrip()
    border = "=" * len(headerrow)
    
    print(border)
    print(headerrow)
    print(border)
    
    for n, x in enumerate(myData):
        row = ["| "]
        row.extend(str(n+1).zfill(4))
        row.extend(" | ")
        for c in columns:
            basewidth = len(x[c])
            if longest[c] >= 10:
                maxwidth = 10
            else:
                maxwidth = longest[c]
            padding = maxwidth - basewidth
            if padding >= 0:
                if x[c].isnumeric():
                    row.extend(" " * padding)
                    row.extend(x[c])
                else:
                    row.extend(x[c])
                    row.extend(" " * padding)
            else:
                row.extend(x[c][0:10])
            row.extend(" | ")
        
        print("".join(row).rstrip())
    
    print(border)
    
    
def measure_columns(data, columns):
    longest = {}
    for c in columns:
        longest[c] = len(c)
    for row in data:
        for field in row:
            if len(row[field]) > longest[field]:
                longest[field] = len(row[field])
    return longest


myData, columns = load_data()
longest = measure_columns(myData, columns)
display_data(myData, columns, longest)