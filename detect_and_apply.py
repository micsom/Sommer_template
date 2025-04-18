#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

TEMPLATES_DIR = Path(".templates")

PROFILE_MAP = {
    "core": ["README.md", "LICENSE", ".github/"],
    "api": ["routes/", "app.py", ".github/workflows/api-check.yml"],
    "ml": ["models/", "notebooks/", ".github/workflows/ml-check.yml"],
    "frontend": ["src/", "vite.config.js", ".github/workflows/frontend-check.yml"],
    "devops": ["terraform/", "Dockerfile", ".github/workflows/devops.yml"],
}

def detect_profiles():
    files = {str(p).lower() for p in Path(".").rglob("*")}
    profiles = {
        "core": any("readme.md" in f or "license" in f or ".github" in f for f in files),
        "api": any("app.py" in f or "routes" in f or "fastapi" in f for f in files),
        "ml": any("models" in f or f.endswith(".ipynb") for f in files),
        "frontend": any("vite" in f or "package.json" in f for f in files),
        "devops": any("terraform" in f or "dockerfile" in f or ".github/workflows" in f for f in files)
    }
    profiles["fullstack"] = profiles["api"] and profiles["frontend"] and profiles["devops"]
    return [p for p, enabled in profiles.items() if enabled]

def apply_profile(profile):
    template_path = TEMPLATES_DIR / profile
    if not template_path.exists():
        print(f"[!] No template found for profile: {profile}")
        return
    for item in template_path.rglob("*"):
        if item.is_file():
            rel_path = item.relative_to(template_path)
            dest_path = Path(".") / rel_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(item, dest_path)
            print(f"[+] Applied {rel_path} from profile '{profile}'")

def main():
    detected = detect_profiles()
    print(f"[✓] Detected Profiles: {', '.join(detected)}")
    for profile in detected:
        apply_profile(profile)

if __name__ == "__main__":
    main()
