# main_analysis.py
import matplotlib.pyplot as plt
from bio_tools import calculate_rpm

def run_pipeline():
    # Define data
    genes = ['Gene_A', 'Gene_B', 'Gene_C']
    reg_counts = [1200, 500, 100]
    scar_counts = [400, 800, 100]
    total = 1000000

    # Calculate RPM using your tool
    reg_rpm = [calculate_rpm(c, total) for c in reg_counts]
    scar_rpm = [calculate_rpm(c, total) for c in scar_counts]

    # Print results
    print("Analysis complete. Check your plot window.")
    
    # Plotting code (Try to type this out from memory if you can!)
    plt.bar(genes, reg_rpm)
    plt.show()

if __name__ == "__main__":
    run_pipeline()
