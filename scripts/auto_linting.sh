#!/bin/bash

# Script that will take all .py files in current dir and run pylint and autopep8

## Hinako Terauchi
## Mar 26 2021

#------------------------------------

# create an empty text file to store the results:
touch lint_results.txt
 
# loop thru each file: 
for file in *.py ; do
	# write the file name getting linted:
	echo ${file} >> lint_results.txt 
	# write the pylint result of the file:
	pylint ${file}  >> lint_results.txt

	# Get the name part of the file (without the .py):
	nameOnly=${file%.py}
	echo ${nameOnly}
	
	# Fix some issues using autopep8 & write into a new file:
	autopep8 ${file} >> "pepedTemp.py"
	
	# run pylint again:
	pylint pepedTemp.py >> lint_results.txt

	# delete the old file, rename the new one as the original name:
	mv pepedTemp.py ${file}
done

