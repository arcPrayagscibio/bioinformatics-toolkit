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

def calculate_rpm(gene_counts, total_reads):
    """Normalizes gene expression by calculating Reads Per Million (RPM).
  This allows you to compare gene expression across different samples."""
  if total_reads == 0:
    return 0.0
  return (gene_counts / total_reads) * 1_000_000

print(f"RPM Value: {calculate_rpm(500,1000000)}")


# bio_tools.py

# (Keep your previous functions here: get_reverse_complement, calculate_gc_content, read_fasta, calculate_rpm)

def get_full_codon_table():
    """Returns the full dictionary of 64 DNA codons and their amino acids."""
    return {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }

def translate_dna(dna_seq):
    """Translates a DNA string into a protein sequence."""
    codon_table = get_full_codon_table()
    protein = []
    # Loop through the sequence in steps of 3
    for i in range(0, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3]
        amino_acid = codon_table.get(codon, "Unknown")
        protein.append(amino_acid)
    return protein



def find_orf(dna_seq):
    start_index = dna_seq.find('ATG')
    if start_index == -1:
        return "No start codon found"
    # Assign coding_seq here, after checking for a start codon
    coding_seq = dna_seq[start_index:]
    return translate_dna(coding_seq)

messy_dna = "GGGGGGGGGGGGATGTTTTTCTAGAAAAAAAAAA"

protein = find_orf(messy_dna)
print(f"detected protein:{protein}")

