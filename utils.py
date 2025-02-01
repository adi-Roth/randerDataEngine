import json

def load_json(file_path: str):
    """Load JSON data from a file."""
    with open(file_path, "r") as f:
        return json.load(f)
