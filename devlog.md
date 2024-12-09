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

#End Session

#Session 2: 12/7/24
##Initial Thoughts:
I have thought about starting on the B tree first since the driver file builds on top of that.
The Btree is responsible for creating the Btree and allocating bytes of memory to each node and header
##Plan:
Create two classes BtreeNode and Btree
    I will work on the insert and create methods first within the Btree class
    I will attempt to get started on the driver file
##Update 8:51
I have created a basic Btree insert command. I will work on a basic create command to and may work the menu for those two on the driver file
##9:42 
new driver file created


