# main_analysis.py

from bio_tools import (
    read_fasta, 
    calculate_gc_content, 
    get_reverse_complement, 
    translate_dna, 
    find_orf
)

def run_full_analysis(file_path):
    print(f"--- Starting Bioinformatics Pipeline: {file_path} ---")
    
    # 1. Read Data
    dna = read_fasta(file_path)
    print(f"Sequence Loaded. Total Length: {len(dna)} bp")
    
    # 2. GC Content Analysis
    gc = calculate_gc_content(dna)
    print(f"GC Content: {gc:.2f}%")
    
    # 3. Reverse Complement (First 50 bases)
    rev_comp = get_reverse_complement(dna)
    print(f"Reverse Complement (50bp): {rev_comp[:50]}...")
    
    # 4. Gene Discovery (ORF Finding)
    # We use a slice of the DNA to look for a gene
    orf_protein = find_orf(dna)
    print(f"Detected ORF Protein Sequence (first 20 amino acids): {orf_protein[:20]}")
    
    print("--- Pipeline Execution Complete ---")

if __name__ == "__main__":
    # Ensure your path points to your actual FASTA file
    target_file = "data/sample_sequence.fasta"
    try:
        run_full_analysis(target_file)
    except FileNotFoundError:
        print(f"Error: File not found at {target_file}. Please check the path.")


