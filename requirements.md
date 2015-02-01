# Requirements

  1. In order to make effective use of csvkit, it is necessary to check first for the presence of control characters in the input data.  This check should be performed first in the following steps:
    a. read the file line by line;
    b. strip out the trailing newline (which is an necessary control char in CSV);
    c. check for each diallowed control char in the line;
    d. if found, report back the character by line and location index.
