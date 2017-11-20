# In our CDM collections, some identifiers were preceded by "00", others were not. This
# eliminates duplicates (images entered twice, one with "00" and once without), and
# appends "00" to the beginning of all remaining files that lacked it.

from sys import argv
import os
    
for filename in os.listdir("."):
    if ('00'+filename) in os.listdir("."):
        print "Duplicate deleted: " + filename
        os.remove(filename)
    elif (not(filename.startswith("00"))):
        print "renamed file: " + filename+ " to 00" +filename
        os.rename(filename, ("00"+filename))
