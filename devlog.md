#12/5/24 14:30
##What I know:
indexing files based on the B-tree data structure

Main functionalities:
creating a new index file
opening an existing index file
insert key/value into index (B-tree operation)
search for a key from index (B-tree operation)
printing the all key/values from the index (B-tree operation)
loading the integers that have been inserted (I/O-read)
extracting the key/value pairs from the index file
exiting the program
most functionalities should have error validation implemented

Index File: 
divided into 512 byte sections
each block stores the B-tree nodes except the first block stores the header

Header:
first 8 bytes: magic number
second 8 bytes: id of the block with root node
third 8 bytes: id of next block to be added to the file

B-tree:
19 key/value pairs
20 child pointers

Project uses sessions and each session to be logged in this file

##Planning:
Create git repository, devlog.md, README.md
use python
multiple files: main driver file, B tree file
