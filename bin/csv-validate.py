#!/usr/bin/env python3

import csv
import subprocess
import sys

datafile = sys.argv[1]
schemafile = sys.argv[2]

def read_spreadsheet(datafile):
    if datafile.endswith(('.xlsx','.xls')):
        cmd = ["in2csv",datafile]
        rawdata = subprocess.check_output(cmd)
        decoded = rawdata.decode('utf-8').split("\n")
        data = [row for row in csv.DictReader(decoded)]
    else:
        with open(datafile, 'r') as f:
            data = [row for row in csv.DictReader(f)]    
    return data

data = read_spreadsheet(datafile)

for row in data:
    print(row)

# columns_to_check = sorted(firstline.split(','))
# required_columns =[ item['name'] for item in mydata]
# 
# for c in required_columns:
#     if c in columns_to_check:
#         print("Found {0}!".format(c))
#     else:
#         print("--> ERROR: {0} not found!".format(c))
#     
