#!/usr/bin/env python3

import csv, pickle, subprocess, sys, yaml

datafile = sys.argv[1]
schemafile = sys.argv[2]
controlchars = pickle.load(open('../lib/control.p', 'rb'))

#= Function ===========
# Load spreadsheet data
#======================
def read_spreadsheet(datafile):
    print('\nLoading spreadsheet data from {0}...'.format(datafile))
    if datafile.endswith(('.xlsx','.xls')):
        cmd = ['in2csv',datafile]
        rawdata = subprocess.check_output(cmd)
        reader = csv.DictReader(rawdata.decode('utf-8').split('\n'))
    else:
        with open(datafile, 'r') as f:
            reader = csv.DictReader(f)
            fields = reader.fieldnames
            data = [row for row in reader]
    return data, fields

#= Function ===========
# Read schema file
#======================
def read_schema(schemafile):
    print('\nLoading schema from {0}...'.format(schemafile))
    with open(schemafile, 'r') as f:
        schema = yaml.load(f)
        return schema

#= Function ===================
# Check for ASCII control chars
#==============================        
def charcheck(mystring, chars):
    for c in chars:
        if c in mystring:
            charlocation = mystring.find(c)
            print('Found {0} at {1}'.format(c, charlocation))

#======================
# Main logic
#======================

## CHECK CONTROL CHARS -- NEED TO DO BEFORE DICTREADER AS CHARS WILL MESS UP PARSING
## 
# with open(inputfile, 'r') as f:
#     for n, line in enumerate(f):
#         print("\nLine {0}".format(n))
#         print("========")
#         line = line.rstrip('\n')
#         print("String -> {0}".format(line))
#         bytes = str.encode(line)
#         print("Bytes -> {0}".format(bytes))
#         charcheck(bytes, [x[0] for x in controlchars])

print('\nLoaded set of ASCII control characters to check.')
print(['{0} : {1}'.format(c[0], c[3]) for c in controlchars])

data, fields = read_spreadsheet(datafile)
print('{0} lines of spreadsheet data loaded.'.format(len(data)))

schema = read_schema(schemafile)
print(schema)

# check for required columns
required = [x['name'] for x in schema if 'required' in x and x['required'] == True]
print('\nRequired Columns: {0}.'.format(', '.join(required)))
print('\nChecking for required columns...')
for c in required:
    if c in fields:
        print('Required column {0} found.'.format(c))
    else:
        print('--> ERROR: Required column {0} not found!'.format(c))
        
# create lists of columns that must be populated  
populated = [x['name'] for x in schema if 'populated' in x and x['populated'] == True]
print('\nPopulated Columns: {0}.'.format(', '.join(populated)))

# create restricted value lists 
value_restricted_cols = {x['name'] : x['values'] for x in schema if 'values' in x}
print('Value restrictions: {0}'.format(value_restricted_cols))


for num, row in enumerate(data):
    print('\nRow {0}:'.format(num))
    # check populated columns
    for pcol in populated:
        if pcol not in row:
            print('--> ERROR: Column {0} must exist AND cannot be empty!'.format(pcol))
        elif row[pcol] == '':
            print('--> ERROR: Column {0} cannot be empty!'.format(pcol))
        else:
            print('Column {0} correctly populated in row {1}.'.format(pcol, num))
    # check column value restrictions
    for vcol in value_restricted_cols:
        if vcol not in row:
            print('--> ERROR: Column {0} must exist AND be in {1}!'.format(vcol,
                value_restricted_cols[vcol]))
        elif row[vcol] not in value_restricted_cols[vcol]:
            print('--> ERROR: Value {0} not valid for column {1}!'.format(row[vcol],
                vcol))
        else:
            print('Column {0} correctly populated in row {1}.'.format(vcol, num))
        

# generate report
#   missing columns
#   missing values by row
#   bad values in columns
