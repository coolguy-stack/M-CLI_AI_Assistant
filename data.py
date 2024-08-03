import os
import json

# Function to read text from TXT files
def read_txt(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return ""

# Parse all TXT files in the given directory
def parse_files(directory):
    texts = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith(".txt"):
            text = read_txt(file_path)
            texts.append(text)
    return texts

# Function to format data into JSONL
def format_to_jsonl(resumes, cover_letters, output_file):
    formatted_data = []
    for resume in resumes:
        for cover_letter in cover_letters:
            # Assuming cover letters contain job descriptions
            prompt = f"Resume: {resume}"
            completion = cover_letter
            formatted_data.append({"prompt": prompt, "completion": completion})
    
    with open(output_file, 'w') as f:
        for entry in formatted_data:
            json.dump(entry, f)
            f.write('\n')

# Directories containing the TXT files
resumes_directory = "resumes"  # Change to your resumes directory path
cover_letters_directory = "cover_letters"  # Change to your cover letters directory path
output_file = "fine_tuning_data.jsonl"

resumes = parse_files(resumes_directory)
cover_letters = parse_files(cover_letters_directory)

format_to_jsonl(resumes, cover_letters, output_file)

print(f"Data has been formatted and saved to {output_file}")
