# Script to rename JPG's pulled from CDM to their DC identifiers. Must run pyoaiharvest to get "xmlfile" arg.
# Credit to Patrick Wallace of Middlebury for writing 99% of this.

from sys import argv
import urllib
import urlparse
import xml.etree.ElementTree as ET

xmlfile = argv[1]
collection_to_dump = argv[2]
outdir = argv[3] #### note: no error checking for if outdir exists; TODO

#Extract URLs

parsed = ET.parse(xmlfile)

for elem in parsed.iter(tag='identifier'):
    pathchunks = urlparse.urlparse(elem.text).path.rsplit(':')[1].split('/')
    if pathchunks[0] == collection_to_dump:
         url = str('http://shudigitallibraries.contentdm.oclc.org/utils/ajaxhelper/?CISOROOT=' 
                   + pathchunks[0] + '&CISOPTR=' + pathchunks[1] 
                   + '&action=2&DMSCALE=100&DMWIDTH='
                   + '10000' + '&DMHEIGHT=' + "10000" 
                   + '&DMX=0&DMY=0')
         urllib.urlretrieve(url, str(outdir + '/' + pathchunks[1] + '.jpg'))
         print ('Retrieved ' + pathchunks[1] + '.jpg')
         
