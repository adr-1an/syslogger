import os
import datetime

# Set the path of the log directory
log_dir = 'logs/'

# Get a list of the log files in the directory
log_files = os.listdir(log_dir)

# Get the total number of log files
total_files = len(log_files)

# Open the output file for writing
output_file = open('output.log', 'w')

# Loop through the log files and read their contents
for i, filename in enumerate(log_files):
    file_path = os.path.join(log_dir, filename)

    # Read the contents of the file
    with open(file_path, 'rb') as f:
        file_contents = f.read()

    # Convert the contents to a human-readable format
    file_contents = file_contents.decode('utf-8')

    # Write the contents to the output file
    output_file.write("File: {}\n\n{}\n\n".format(filename, file_contents))

    # Print the progress of the operation
    progress = (i + 1) / total_files * 100
    print("Processed file {}/{} - {:.2f}%".format(i+1, total_files, progress))

# Close the output file
output_file.close()

