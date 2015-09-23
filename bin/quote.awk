BEGIN 	{	FS = "\t"; OFS = ",";
			print "["
			}

NR > 1	{	print "(b'\\x" $4 "', '" $5 "', '" $6 "', '" $7 "', '" $9 "'),"
			}
			
END		{	print "]"
			}
