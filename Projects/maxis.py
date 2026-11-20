import os

def find_largest_file_everywhere():
    # Start at the directory where you run this script
    start_dir = os.getcwd()
    
    largest_file_path = None
    max_size = -1

    print(f"Scanning '{start_dir}' and all subfolders...\n")

    # os.walk automatically recurses through all subdirectories
    for root, dirs, files in os.walk(start_dir):
        for filename in files:
            # Join the folder path with the filename to get the full path
            full_path = os.path.join(root, filename)
            
            try:
                # Get file size in bytes
                file_size = os.path.getsize(full_path)
                
                if file_size > max_size:
                    max_size = file_size
                    largest_file_path = full_path
                    
            except (FileNotFoundError, PermissionError):
                # Safely skip hidden system files or restricted folders
                continue

    # Print the final result
    if largest_file_path:
        size_mb = max_size / (1024 * 1024)
        print("=" * 50)
        print("WINNER: Largest File Found")
        print("=" * 50)
        print(f"Path: {largest_file_path}")
        print(f"Size: {size_mb:.2f} MB ({max_size:,} bytes)")
    else:
        print("No files found in this directory or any subfolders.")

if __name__ == "__main__":
    find_largest_file_everywhere()
