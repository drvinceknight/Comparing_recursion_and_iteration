all: binary_mean.png factorial.png

binary_mean.png: binarysearch.csv recursivebinarysearch.csv
	./Analyse.py

factorial.png: factorial.csv
	./Analyse_factorial.py
