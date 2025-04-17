#!/usr/bin/env python3
import os
import json
from pathlib import Path

def detect_profile():
    # Collect all file paths in lowercase for case-insensitive matching
    files_set = set(str(p).lower() for p in Path('.').rglob('*'))

    # Define profiles and their detection logic
    profiles = {
        'core': any(x in files_set for x in ['readme.md', 'license', '.github']),
        'api': any(x in files_set for x in ['main.py', 'app.py', 'routes']) or 
               any(keyword in f for keyword in ['fastapi', 'flask'] for f in files_set),
        'ml': any(x in files_set for x in ['models', 'dvc.yaml']) or 
              any(f.endswith('.ipynb') for f in files_set),
        'frontend': any(x in files_set for x in ['package.json', 'vite.config.js', 'src']) or 
                    any(keyword in f for keyword in ['react', 'vue'] for f in files_set),
        'devops': any(x in files_set for x in ['dockerfile', 'terraform', 'helm', '.github/workflows']),
    }

    # Detect fullstack profile if all relevant profiles are present
    profiles['fullstack'] = profiles['api'] and profiles['frontend'] and profiles['devops']

    # Collect detected profiles
    detected_profiles = [profile for profile, is_detected in profiles.items() if is_detected]

    # Output detected profiles as JSON
    print(json.dumps({'profiles': detected_profiles}, indent=2))

    return detected_profiles

if __name__ == '__main__':
    detect_profile()
