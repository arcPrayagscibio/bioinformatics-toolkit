def get_reverse_complement(sequence):
    """Computes the reverse complement of a DNA sequence."""
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement_seq = ""
    for base in reversed(sequence):
        reverse_complement_seq += complement_map.get(base, base)
    return reverse_complement_seq

# 1. Define the path to the uploaded file
my_fasta_file = "/content/sample.fasta.txt"

# 2. Extract the DNA
dna_data = read_fasta(my_fasta_file)

# 3. Analyze it
rev_comp = get_reverse_complement(dna_data)

print(f"Extracted Sequence Length: {len(dna_data)}")
print(f"First 20 bases: {dna_data[:20]}")
print(f"Reverse Complement: {rev_comp[:20]}...")
