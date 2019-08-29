# Hybrid-phage-genome-sequence-analysis
For Hybrids 1-8, Sanger sequencing reads covering their coding regions were manually assembled using SnapGene software. For Hybrids 9-18, a single read covered the region of interest, therefore no assembly was required. Sequences for each set of hybrids (1-8 and 9-18) were aligned with corresponding genomic regions in Andhra and JBug18 using the Clustal Omega Multiple Sequence Alignment tool (https://www.ebi.ac.uk/Tools/msa/clustalo/). The sequence alignments (Supplementary files 1 and 2) were analyzed by a Python script developed in-house which first scans the alignment of JBug18 and Andhra, identifies each position of non-similarity, and then determines at those positions the fraction of hybrids that possess Andhra identity. The output data was exported into an Excel file, and the graphs showing the fraction of hybrids with Andhra identity at each position were generated using Microsoft Excel.

# How to Run the Code

The output file produced by the Clustal Omega Multiple Sequence Alignment tool will be in fasta format. Each of these input files must be appended with '.txt' extention before analysis. For example, if the file name is 'Hybrids_1-8_alignment.clustal_num', it should be changed to 'Hybrids_1-8_alignment.clustal_num.txt' before running the code.

Place this sequence file in the same folder where MainScript.py resides. In MainScript.py, edit line 41 (line = read_file('...')) and paste the sequnce file name. Include the '.txt' file extension. After running the codde, the results will be reported as a csv file named 'Analysis_Results.csv', which can be found in the same folder.

Note that  MainScript.py requires the Pandas package to be installed.

Two examplar sequence files are included for analysis: 'Hybrids_1-8_alignment.clustal_num' and 'Hybrids_9-18_alignment.clustal_num'.
