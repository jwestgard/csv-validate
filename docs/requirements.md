# Requirements

  1. In order to make effective use of csvkit, it is necessary to check first for the presence of control characters in the input data.  This check should be performed first in the following steps:
    - read the file line by line;
    - strip out the trailing newline (which is an necessary control char in CSV);
    - check for each diallowed control char in the line;
    - if found, report back the character by line and location index.
  
  2. Use csvstat to check the contents of the input.  
  
  3. Use csvclean to cleanup the input data.
  
  4. Load schema file and check data against the schema. Schema file should be a yaml file for easy creation by users.
  
  5. Generate report.
  
