#!/bin/bash
for FILENAME in *.py
do
	echo "Testing "$FILENAME
	pylint --include-ids=y "$FILENAME" > ../../testResults/${FILENAME%.*y}TestResults
done
