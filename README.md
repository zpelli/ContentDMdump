# ContentDMdump

To begin, we used pyoaiharvest (https://github.com/vphill/pyoaiharvester) to get an XML file containing the metadata for our collections.

We then used JPGdump.py to pull the images out of CDM. Credit to Patrick Wallace of Middlebury College for this one (http://sites.middlebury.edu/archivistslab/dumping-contentdm-collections-for-migration-the-basics/).

The other scripts (00dedup.py and DCrename.py) were used to clean up the odds and ends. They renamed the files to their respective DC identifiers, removed duplicate files, and made the filenames consistant.

This was my first experience with python, so these are open to improvement and simplification.

If you have any question on the use of then, contact me at zachary.pelli@shu.edu.
