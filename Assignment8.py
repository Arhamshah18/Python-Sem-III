input_filename = "input.txt"
output_filename = "output.txt"

# Sample file creation for demonstration
with open(input_filename, "w") as f:
    f.write("Line 1: First header line\nLine 2: Second detail line\nLine 3: Third unused line\nLine 4: Fourth line")

# Read input file, count lines, and extract first two lines
with open(input_filename, "r") as f_in:
    lines = f_in.readlines()

total_lines = len(lines)
first_two_lines = lines[:2]

# Write extracted lines to new file
with open(output_filename, "w") as f_out:
    f_out.writelines(first_two_lines)

print(f"Total lines in '{input_filename}': {total_lines}")
print(f"Successfully wrote the first 2 lines to '{output_filename}'.")
