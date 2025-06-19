import os

def find_and_delete_empty_files(start_path):
    """
    Finds empty files (0 bytes) within a given directory and its subdirectories,
    excluding files named '__devonly__.py', and deletes them.

    Args:
        start_path (str): The starting directory to search.

    Returns:
        tuple: A tuple containing two lists:
               - deleted_files (list): Paths of files that were deleted.
               - skipped_files (list): Paths of __devonly__.py files that were skipped.
    """
    deleted_files = []
    skipped_files = []
    
    print(f"Searching for empty files in: {start_path} and its subfolders...")
    print("WARNING: This script will DELETE empty files (excluding __devonly__.py).")
    print("         Ensure you have backed up any critical data before proceeding.")
    print("-" * 60)

    for root, _, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            if file == '__devonly__.py':
                skipped_files.append(file_path)
                continue # Skip __devonly__.py files
            
            if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"DELETED: {file_path}")
                except OSError as e:
                    print(f"ERROR: Could not delete {file_path} - {e}")
            # else:
            #     # Optional: Uncomment the line below if you want to see files that are not empty or are not regular files
            #     # print(f"SKIPPED (not empty or not file): {file_path}")
    
    return deleted_files, skipped_files

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # IMPORTANT: Before running this, consider testing in a dummy folder
    # or uncommenting the line below and changing it to a specific test path:
    # script_dir = "/path/to/your/test/folder" 
    
    # CONFIRMATION STEP: Highly recommended to avoid accidental deletion
    print("\n")
    user_confirm = input(f"Are you sure you want to delete empty files in '{script_dir}' and its subfolders? (yes/no): ").lower().strip()

    if user_confirm == 'yes':
        deleted_files, skipped_files = find_and_delete_empty_files(script_dir)

        print("\n" + "=" * 60)
        print("Deletion Summary:")
        print("=" * 60)

        if deleted_files:
            print(f"\nSuccessfully deleted {len(deleted_files)} empty files:")
            for f in deleted_files:
                print(f"- {f}")
        else:
            print("\nNo empty files were found and deleted.")

        if skipped_files:
            print(f"\nSkipped {len(skipped_files)} '__devonly__.py' files:")
            for f in skipped_files:
                print(f"- {f}")
        else:
            print("\nNo '__devonly__.py' files were encountered.")

        print("\nOperation complete.")
    else:
        print("\nOperation cancelled by user. No files were deleted.")