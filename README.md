# bioinformatics-toolkit
This repository contains modular tool for genetic analysis 

## :contents:-

'read_fasta()':function to handle real-world genetic data, filtering out headers and cleaning whitespace.

'calculate_gc_content()': A standard metric for identifying organisms and genome reasearch.

'get_reverse_complement()': A script for reverse sequence generation, Essential for DNA sequencing analysis.

'translate_dna()':  molecular decoder, a script to translate dna into amino acid chains, using a full 64 codon dictionary .

'find_orf()': gene-discovery engine, its scans a dna then finds first ATG(start codon) and ends with a stop codon(TAA TAG TGA).

## projects 
'bio_toosl.py':- library containing all analytical functions


'main_analysis.py ':- this file contains all analysis done till now


'data/':- Directory for storing raw FASTA files.

## Future Development
Currently exploring integration with real-world public databases (NCBI) and simulating mutation effects (point mutations and frameshifts) on protein structure.






