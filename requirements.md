# Requirements

  1. In order to make effective use of csvkit, it is necessary to check first for the presence of control characters in the input data.  This check should be performed first in the following steps:
  
    1. read the file line by line;
    2. strip out the trailing newline (which is an necessary control char in CSV);
    3. check for each diallowed control char in the line;
    4. if found, report back the character by line and location index.
