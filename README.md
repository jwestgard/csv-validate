Validation of tabular (CSV) data against a schema defined in YAML or JSON. See the schema.yml file in this repository for an example and instructions on creating a schema. It is possible to designate up to six main "rules":

  1. required columns (i.e. columns that must exist for all rows)
  2. allowed columns (i.e. *only* the specified columns can exist -- for strict control of data)
  3. populated columns (i.e. these columns must contain a non-null value)
  4. controlled values (specify a set of possible values as a list in the form: {'colname' : ['val1','val2','val3']}
  5. numeric data (cells in these columns may only contain digits)
  6. date data (values in these columns must be parsable as ISO-8601 dates)
