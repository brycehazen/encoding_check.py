import os
import chardet
import pandas as pd
import time
import itertools

def detect_encoding(file_path):
    # Open the file as binary and read all content for accurate encoding detection
    with open(file_path, 'rb') as f:
        raw_data = f.read()  # Read entire file
        result = chardet.detect(raw_data)
        return result['encoding']

def list_csv_files():
    # List all CSV files in the current directory
    csv_files = [filename for filename in os.listdir('.') if filename.endswith('.csv')]
    
    # Display the list of CSV files with numbering
    print("Select the file(s) by entering the numbers separated by commas:")
    for i, filename in enumerate(csv_files, start=1):
        print(f"{i}.) {filename}")
    
    # Prompt the user to select files
    selected_numbers = input("Enter the numbers of the files you want to process (e.g., 1,3,4): ")
    selected_indices = [int(num.strip()) - 1 for num in selected_numbers.split(',') if num.strip().isdigit()]
    
    # Filter the selected files
    selected_files = [csv_files[i] for i in selected_indices if 0 <= i < len(csv_files)]
    return selected_files

def process_csv_files():
    selected_files = list_csv_files()
    
    if not selected_files:
        print("No files selected or invalid selection.")
        return
    
    # Cycle for the loading animation
    dots = itertools.cycle(['.', '..', '...', '....', '.....', '....', '...', '..', '.'])
    
    # Process each selected CSV file with animation
    for i, filename in enumerate(selected_files, start=1):
        # Print the processing status with cycling dots
        print(f"Processing file {i} of {len(selected_files)}: {filename}", end="")
        
        for _ in range(10):  # Set duration for the animation
            print(next(dots), end="\r", flush=True)
            time.sleep(0.2)
            print(f"\rProcessing file {i} of {len(selected_files)}: {filename}", end="")

        # Detect encoding
        encoding = detect_encoding(filename)
        time.sleep(0.5)  # Brief pause before showing results for readability
        
        # Print results for this file
        if encoding:
            print(f"\rFile: {filename}, Encoding: {encoding}")
        else:
            print(f"\rCould not determine encoding for {filename}")

        # Additional line break for separation before the next file
        print()

# Run the script
process_csv_files()
