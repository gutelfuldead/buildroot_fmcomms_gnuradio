#!/bin/python

# convert .mat file to a c file array

import sys
import scipy.io as spio

def convert_to_c(inputFile):
	fileNew = spio.loadmat(inputFile, appendmat=False)
	print type(fileNew)

	for key in fileNew:
		print key

	outputFileName = inputFile.replace(".mat",".c")
	wavName = outputFileName.split('.')[0]

	# fp = open(outputFileName,"w")
	# fp.write("uint16_t "+wavName+"[NSAMPLES] =\n{")

	return outputFileName

if __name__ == "__main__":
		if(len(sys.argv) != 2):
			print "Must provide input mat file..."
			print sys.argv[0],"LTE10.mat"
			sys.exit()

		newName = convert_to_c(sys.argv[1])
		print "Generated ",newName