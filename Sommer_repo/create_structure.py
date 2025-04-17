import os

base_path = "/Users/michaelsommer/Downloads/NEW2025/Sommer_repo/.templates"

structure = {
    "api/.github/workflows/api-check.yml": "",
    "ml/.github/workflows/ml-check.yml": "",
    "frontend/.github/workflows/frontend-check.yml": "",
    "devops/.github/workflows/devops.yml": "",
    "core/README.md": "",
    "core/LICENSE": "",
    "core/.github/settings.yml": "",
}

for relative_path, content in structure.items():
    file_path = os.path.join(base_path, relative_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        file.write(content)
