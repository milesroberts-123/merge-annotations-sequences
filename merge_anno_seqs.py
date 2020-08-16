import re
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

#Write input and output files
annofile = sys.argv[1]
seqfile = sys.argv[2]
outfile = sys.argv[3]

#Load annotations as dictionary
print("Thank you for using this script!")
print("USAGE: python3 merge_anno_seqs.py <TSV FILE OF ANNOTATIONS> <FASTA FILE OF SEQUENCES> <OUTPUT FILE NAME>")

print("Loading annotations in %s ..." % annofile)
annofile = open(annofile, "r")
list = annofile.readlines()

annodict = dict()
for element in list:
	parts = element.split("\t")
	id = parts[0]
	anno = parts[1]
	anno = re.sub("\r\n", "", anno)
	annodict[id] = anno


#Load in sequences as dictionary
#For each sequence, extract the appropriate annotation
print("Matching annotations to sequences in %s ..." % seqfile)
newseqrecords = []
for seqrecord in SeqIO.parse(seqfile, "fasta"):
	newseqrecord = SeqRecord(seqrecord.seq, id = seqrecord.id, description = annodict[seqrecord.id])
	newseqrecords.append(newseqrecord)

print("Writing %i records to %s ..." % (len(newseqrecords), outfile))
SeqIO.write(newseqrecords, outfile, "fasta")

print("Merge complete.")
print("Please leave me a star on github if you use this script!")
print("Check out my other useful scripts here: https://github.com/milesroberts-123?tab=repositories")
