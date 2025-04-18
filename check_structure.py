import os

# Define the expected structure
EXPECTED_STRUCTURE = {
    ".templates": {
        "api": [".github/workflows/api-check.yml"],
        "ml": [".github/workflows/ml-check.yml"],
        "frontend": [".github/workflows/frontend-check.yml"],
        "devops": [".github/workflows/devops.yml"],
        "core": ["README.md", "LICENSE", ".github/settings.yml"],
    }
}

def validate_structure(base_path, structure):
    errors = []
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        if not os.path.isdir(folder_path):
            errors.append(f"Missing directory: {folder_path}")
            continue
        for file in files:
            file_path = os.path.join(folder_path, file)
            # Check for nested directories in file paths
            if "/" in file:
                nested_dir = os.path.dirname(file_path)
                if not os.path.isdir(nested_dir):
                    errors.append(f"Missing directory: {nested_dir}")
                    continue
            if not os.path.exists(file_path):
                errors.append(f"Missing file: {file_path}")
    return errors

if __name__ == "__main__":
    base_path = "/Users/michaelsommer/Downloads/NEW2025/Sommer_repo/.templates"
    errors = validate_structure(base_path, EXPECTED_STRUCTURE)
    if errors:
        print("Validation Errors:")
        for error in errors:
            print(f" - {error}")
    else:
        print("All files and directories are correctly placed.")
