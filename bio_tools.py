# bio_tools.py

def get_reverse_complement(dna_seq):
    """
    Takes a DNA sequence, returns its reverse complement.
    Uses str.maketrans for fast translation.
    """
    # Standardize to uppercase
    dna_seq = dna_seq.upper()
    
    # 1. Translate to complement
    translation_table = str.maketrans("ATGC", "TAGC")
    complement = dna_seq.translate(translation_table)
    
    # 2. Reverse the string
    return complement[::-1]

def calculate_gc_content(dna_seq):
    """
    Calculates the percentage of G and C bases in a DNA sequence.
    """
    dna_seq = dna_seq.upper()
    g_count = dna_seq.count('G')
    c_count = dna_seq.count('C')
    total = len(dna_seq)
    
    if total == 0:
        return 0.0
     
    return ((g_count + c_count) / total) * 100
    
    def read_fasta(file_path):
    """Reads a fasta file and returns the DNA sequence as a single string."""
    sequence = ""
    with open(file_path, 'r') as file:
        for line in file:
            # Skip the header line
            if line.startswith(">"):
                continue
            # Remove newline characters and append to sequence
            sequence += line.strip()
    return sequence.upper()
