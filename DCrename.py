# Script to rename JPG's pulled from CDM to their DC identifiers (to link them to DC metadata).
# Must run pyoaiharvest to get "xmlfile" arg.

from sys import argv
import xml.etree.ElementTree as ET
import os

xmlfile = argv[1]
collection_id = argv[2]

parsed = ET.parse(xmlfile)
root = parsed.getroot()

i = 0

namespaces = {'dc': 'http://purl.org/dc/elements/1.1/'}
    
for filename in sorted(os.listdir("."), key=lambda x: int(x.split('.')[0])):
    if root[i][0].get('status')=='deleted':             # deletes dummy jpg's that result from "status: deleted" oai records
        os.remove(filename)
        print 'pic removed'
    elif (collection_id in root[i][0][0].text):
        dcID = root[i][1][0].find('dc:identifier', namespaces).text+ '.jpg'  
        if (dcID) not in os.listdir("."):            
            os.rename(filename, dcID)       # renames files to their DC identifiers 
            print "Valid record, DC id: " + dcID
        else:
            print "Duplicate (" +filename+ ") removed"
            os.remove(filename)                   # deletes duplicate files
    i+=1
         
