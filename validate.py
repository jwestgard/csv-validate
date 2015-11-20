#!/usr/bin/env python3

import argparse
import csv
from dateutil.parser import parse
import os
import pickle
import subprocess
import sys
import yaml

#= Function ===========
# Load spreadsheet data
#======================
def read_spreadsheet(datafile):
    print('Loading spreadsheet data from file "{0}" ... '.format(
        datafile), end='')
    if datafile.endswith(('.xlsx','.xls')):
        print('converting Excel ... ', end='')
        cmd = ['in2csv',datafile]
        rawdata = subprocess.check_output(cmd)
        reader = csv.DictReader(rawdata.decode('utf-8').split('\n'))
        cols = reader.fieldnames
        data = list(reader)
    else:
        with open(datafile, 'r') as f:
            reader = csv.DictReader(f)
            cols = reader.fieldnames
            data = list(reader)
    print("complete.")
    return cols, data

#= Function ======
# Read schema file
#=================
def read_schema(schemafile):
    print('Loading schema from file "{0}" ... '.format(schemafile), end='')
    with open(schemafile, 'r') as f:
        schema = yaml.load(f)
    print("{0} main rules loaded.".format(len(schema)))
    return schema

#= Function ===============
# Pull data from Excel File
#==========================
def convert_excel(excelfile):
    bashCommand = "in2csv {0}".format(excelfile)
    return subprocess.check_output(bashCommand.split())

#= Function ===================
# Check for ASCII control chars
#==============================
def charcheck(rawlines):
    with open('control.p', 'rb') as f:
        chars = pickle.load(f)
    print('\nChecking raw bytes for control characters other than newlines ...')
    for n, rawline in enumerate(rawlines):
        for c in chars:
            if c[0] in rawline and c[3] != "^J":
                charlocation = rawline.find(c[0])
                print('\tFound {0} ({1}) at {2} in line {3}'.format(c[4],
                    c[3], charlocation, n))

#= Function ==================
# Validate data against schema
#=============================
def validate(colnames, data, schema):
    violations = {}
    result = []
    for rule_num, rule in enumerate(schema):
        violations[rule] = []

        # require specified columns
        if rule == 'required':
            print("{0}. Checking for required columns ... ".format(
                rule_num+1), end='')
            for reqcol in schema['required']:
                if reqcol not in colnames:
                    violations[rule].append(
                        "Column {0} is required.".format(reqcol))

        # disallow any columns not specified
        elif rule == 'allowed':
            print("{0}. Checking allowed columns ... ".format(
                rule_num+1), end='')
            for col in colnames:
                if col not in schema['allowed']:
                    violations[rule].append(
                        "Column '{0}' not in allowed cols list".format(col))

        # require columns to be populated
        elif rule == 'populated':
            print("{0}. Checking for populated columns ... ".format(
                rule_num+1), end='')
            for row_num, row in enumerate(data):
                for popcol in schema['populated']:
                    if row[popcol] == '':
                        violations[rule].append(
                            "Column '{0}' is empty in row {1}.".format(
                                popcol, row_num+2))
        
        # require columns to contain numeric data only
        elif rule == 'numeric':
            print("{0}. Checking numeric columns ... ".format(
                rule_num+1), end='')
            for row_num, row in enumerate(data):
                for numcol in schema['numeric']:
                    try:
                        row[numcol] = int(row[numcol])
                    except ValueError:
                        violations[rule].append(
                            "Column '{0}' in row {1} is not numeric.".format(
                                numcol, row_num+2))
                                
        # require parseable date string
        elif rule == 'date':
            print("{0}. Checking date columns ... ".format(
                rule_num+1), end='')
            for row_num, row in enumerate(data):
                for datcol in schema['date']:
                    try:
                        parse(row[datcol])
                    except ValueError:
                        violations[rule].append(
                            "Column '{0}' in row {1} is not a date.".format(
                                datcol, row_num+2))
        
        # require values from controlled value list
        elif rule == 'controlled':
            print("{0}. Checking controlled values ... ".format(
                rule_num+1), end='')
            for row_num, row in enumerate(data):
                for concol in schema['controlled']:
                    if row[concol] not in schema['controlled'][concol]:
                        violations[rule].append(
                            "Column '{0}' in row {1} has illegal value.".format(
                                concol, row_num+2))
        
        # raise an error for non-conforming schema entries
        else:
            violations.append("Schema error: '{0}' not valid.".format(rule))
            
        # report success or failure of each rule evaluation
        if violations[rule]:
            print("failed!")
            result.extend([v for v in violations[rule]])
        else:
            print("passed.")
        
    return result
    
#===========
# Main logic
#===========
# parse arguments
parser = argparse.ArgumentParser(description='Validate Tabular Data')
parser.add_argument('--schema', '-s', action='store', 
    help='path to schema file to validate against')
parser.add_argument('--output', '-o', action='store', 
    help='path to outputfile (for cleaned data)')
parser.add_argument('filename', help='data file to be validated or cleaned')
args = parser.parse_args()

# print output header
print("")
border = "=" * 40
print("\n".join([border, "# VALIDATE.PY: TABULAR DATA VALIDATION #", border]))

# load data
datafile = args.filename
colnames, data = read_spreadsheet(datafile)

# report stats
print("Data has {0} columns and {1} rows.".format(len(colnames), len(data)))

# load schema and validate
if args.schema:
    schema = read_schema(args.schema)
    violations = validate(colnames, data, schema)
    if violations:
        print("\nResult: Failure")
        print("===============")
        for n, v in enumerate(violations):
            print("{0}. {1}".format(n+1, v))
            print("")
    else:
        print("Result: Successful Validation!\n")
         
# save output file
# check encoding and convert to utf8

