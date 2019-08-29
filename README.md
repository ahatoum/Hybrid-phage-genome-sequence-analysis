# Hybrid-phage-genome-sequence-analysis
For Hybrids 1-8, Sanger sequencing reads covering their coding regions were manually assembled using SnapGene software. For Hybrids 9-18, a single read covered the region of interest. Sequences for each set of hybrids (1-8 and 9-18) were aligned with corresponding genomic regions in Andhra and JBug18 using the Clustal Omega Multiple Sequence Alignment tool (https://www.ebi.ac.uk/Tools/msa/clustalo/), and the sequence alignment (.clustal_num) was used as input (Supplementary files 1 and 2) for a Python script (developed in-house) which scans the alignment of JBug18 and Andhra, identifies each position of non-similarity, and determines at those positions the fraction of hybrids that possess Andhra identity at that position

# How to Run the Code

Place the sequence file in the same folder where MainScript.py resides. In MainScript.py, edit line 41 (line = read_file('...')) and paste the sequnce file name. Include the '.txt' file extension.
