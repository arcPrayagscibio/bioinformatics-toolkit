# Project: Gene Expression Analysis
# Goal: Compare gene activity between regenerating and scar tissue.

from bio_tools import calculate_rpm

# Data for our genes
regenerating_counts = {"Gene_A": 1200, "Gene_B": 500, "Gene_C": 100}
scar_counts = {"Gene_A": 400, "Gene_B": 800, "Gene_C": 100}
total_reads = 1000000

print("--- RPM Expression Results ---")
for gene in regenerating_counts:
    reg_rpm = calculate_rpm(regenerating_counts[gene], total_reads)
    scar_rpm = calculate_rpm(scar_counts[gene], total_reads)
    print(f"{gene}: Regenerating={reg_rpm:.0f}, Scar={scar_rpm:.0f}")
