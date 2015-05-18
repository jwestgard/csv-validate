# Requirements

  1. The ultimate goal is to allow for the validation of CSV data according to a flexible set of rules defined in a schema file.
  2. The tool must deal elegantly with non-printing control characters that often creep into CSV files when exported from Excel.
  3. The tool should produce reports of anomalies (violations of schema) and statistics about CSV data.
  4. The tool should allow the user to make batch corrections to data, and should facilitate the correction of anomalies in the data.
  5. The tool should allow for local correction and validation of CSV data before import into other systems.


## Use Case: Audio/Video Batch Loader

The xml generator script needs to perform additional validation of the metadata before ingest in order to ensure that the ingested audio objects will be compatible with the digital collections admin interface.

Currently, it is possible to create XML files that omit required elements, and Fedora will allow these items to exist, but when such an item is opened in the admin interface, omitted items can lead to unexpected results, such as defaulting to 21st century the covTime element.

Items that should be validated include:

   - dates in ISO format (YYYY, YYYY-MM, or YYYY-MM-DD)
   - century must be populated in form YYYY-YYYY
   - mediatype must be populated
   - browse terms must be present for all AlbUM items
   - XMLType fields must be populated (for all rows to be ingested), and if multi-rowed metadata layout, each UMDM must have at least one UMAM

The script should enable validation to happen separately from the ingest (pre-validation), and should create a validation report, summarizing the batch and listing each non-conformant line of data.


## Pseudocode

  1. Check first for the presence of control characters in the input data.  This check should be performed first in the following steps:
    - read the file line by line;
    - strip out the trailing newline (which is an necessary control char in CSV);
    - check for each diallowed control char in the line;
    - if found, report back the character by line and location index.
  
  2. Use csvstat to check the contents of the input.  
  
  3. Use csvclean to cleanup the input data.
  
  4. Load schema file and check data against the schema. Schema file should be a yaml file for easy creation by users.
  
  5. Generate report.
