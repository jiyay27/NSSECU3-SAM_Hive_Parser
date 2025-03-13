import os
import subprocess
import sys

RECMD_PATH = ".\\RECmd\\RECmd.exe"  # Path to RECmd.exe
BATCH_FILE = ".\\RECmd\\BatchExamples\\SAM.reb"  # Path to batch file for parsing SAM
OUTPUT_DIR = ".\\Output"  # Output directory for CSV results
CSV_FILENAME = "sam_parsed_results.csv"  # Output CSV file name

def parse_sam_hive(sam_hive_path):
    if not os.path.exists(sam_hive_path):
        print(f"Error: SAM hive file '{sam_hive_path}' does not exist.")
        return
    
    if not os.path.exists(RECMD_PATH):
        print(f"Error: RECmd not found at '{RECMD_PATH}'. Make sure it's installed.")
        return
    
    if not os.path.exists(BATCH_FILE):
        print(f"Error: RECmd batch file '{BATCH_FILE}' not found. Check the path.")
        return

    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Define full output CSV path
    csv_output_path = os.path.join(OUTPUT_DIR, CSV_FILENAME)

    # Construct RECmd command
    recmd_command = f'"{RECMD_PATH}" -f "{sam_hive_path}" --bn "{BATCH_FILE}" --csv "{OUTPUT_DIR}" --csvf "{CSV_FILENAME}"'

    try:
        print(f"Running RECmd on SAM hive: {sam_hive_path}")
        subprocess.run(recmd_command, shell=True, check=True)
        print(f"Parsing complete! CSV output saved at: {csv_output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running RECmd: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_sam_recmd.py <SAM_HIVE_PATH>")
        sys.exit(1)

    sam_hive_path = sys.argv[1]
    parse_sam_hive(sam_hive_path)


