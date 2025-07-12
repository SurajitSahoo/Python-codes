def copy_without_comments(source_file, destination_file):
    with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
        for line in src:
            if not line.strip().startswith('#'):  # Skip comment lines
                dest.write(line)

# Example usage
source = 'source_script.py'  # Replace with your source file path
destination = 'destination_script.py'  # Replace with your destination file path
copy_without_comments(source, destination)
