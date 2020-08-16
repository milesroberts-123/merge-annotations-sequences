# merge-annotations-sequences

Merge a list of functional annotations with a fasta file of sequences

Often times, functional annotations (statements on the potential function of gene products) are stored seperately from sequences. In some analyses, however, it is preferable to have functional annotations and sequences in the same file. This script accomplishes just that!

## USAGE

The syntax for this script is as follows:

`python3 merge_anno_seqs.py <TSV FILE OF ANNOTATIONS> <FASTA FILE OF SEQUENCES> <OUTPUT FILE NAME>`

How do you make a tab-seperated list of functional annotations? Check out my [extract-annotations script](https://github.com/milesroberts-123/extract-annotations).

For example, this code:

`python3 merge_anno_seqs.py my_example_annotations.txt my_example_proteins.fasta my_example_merged.fasta`

will take the annotations in my_example_annotations.txt, merge them to the sequences stored in my_example_proteins.fasta, and save the output to my_example_merged.fasta.

## FORMAT

The first input to this script is a tab-seperated list of each gene and its corresponding functional annotation. The first column contains the gene identifiers and the second column contains the annotations. For example:

```
gene1      transcription factor
gene2      unknown protein
...
gene3      heat shock protein
```

The second input is a list of sequences in [FASTA format](https://en.wikipedia.org/wiki/FASTA_format).

The output of the script will be a FASTA format sequences file, except now annotations will be included in header lines:

```
>gene1 transcription factor
HGTVILLVYVDDIIITGFTAALIEDVTRAMHTTFKMKDLGSLHYFLGMEVSRIGSGLFLH
QSKYARDLLQKAGLEKCTSQPTLMAVSSSTNGADTPFADITHFCSLIGALQYLAITRPDI
QFAVNRVAQRMHQPSEHDYHCLKRILRYIFGTLGRGLLIRPGDLELRGFSDSDWANDKND
RKSTSRFLVFLGPNLISWCTKKQPKVSRSSTEAEYRAVALLAAETMW
>gene2 unknown protein
MPISPSRSTNSVDVPFHNPRLFHSLVGGLQYLTVTRPDIQFAVNYVAQKMHSLTEQDFHT
LKRILRYVKGIILCGLIFSKGDLRLRGYSNSDWANDPSDNCSTTDYLIFFGPNLISWNTE
KQGRVSKSSTEAEYRALSAAASEV
...
```

This resulting fasta file can still be parsed by other software, like [Biopython](https://biopython.org/wiki/Download).

## DEPENDENCIES

1. Biopython. Install with:

`pip install biopython`

If that doesn't work, see [here](https://biopython.org/wiki/Download).

2. Python3 - I tested this script with Python v3.8.2

## REFERENCES

I acquired the example genes and annotations from the [Sol Genomics Network](https://solgenomics.net/organism/Solanum_lycopersicum/genome).
