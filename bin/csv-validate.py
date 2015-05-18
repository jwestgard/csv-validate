#!/usr/bin/env python3

import csv
import subprocess
import sys
import yaml

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

def read_schema(schemafile):
    with open(schemafile, 'r') as f:
        schema = yaml.load(f)
        return schema

data = read_spreadsheet(datafile)
schema = read_schema(schemafile)
required_cols = [x['name'] for x in schema if 'required' in x.items()]
populated_cols = [x['name'] for x in schema if 'populated' in x.items()]

print("Required Columns: {0}".format(', '.join(required_cols)))
print("Populated Columns: {0}".format(', '.join(populated_cols)))

# columns_to_check = sorted(firstline.split(','))
# required_columns =[ item['name'] for item in mydata]
# 
# for c in required_columns:
#     if c in columns_to_check:
#         print("Found {0}!".format(c))
#     else:
#         print("--> ERROR: {0} not found!".format(c))
#     
