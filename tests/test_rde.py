import os
import json
import pytest
from randerDataEngine.rde import RanderDataEngine

# Initialize RDE Engine
engine = RanderDataEngine()

# Load test data
TEST_DATA_PATH = "tests/data_example.json"
TEMPLATE_NAME = "package.json.j2"
TEMPLATE_GROUP = "nodejs"
OUTPUT_FILE = "tests/output_package.json"

@pytest.fixture
def load_test_data():
    """Loads the JSON test data"""
    with open(TEST_DATA_PATH) as f:
        return json.load(f)

def test_single_render(load_test_data):
    """Test rendering a single template"""
    result = engine.render_template(f"{TEMPLATE_GROUP}/{TEMPLATE_NAME}", load_test_data)
    
    assert '"name": "my-node-project"' in result
    assert '"express": "^4.18.2"' in result
    assert '"jest": "^29.0.0"' in result  # Dev dependency

    # Save the output for review
    with open(OUTPUT_FILE, "w") as f:
        f.write(result)

def test_dry_run_render(load_test_data, capsys):
    """Test dry-run mode (prints instead of writing)"""
    engine.render_template(f"{TEMPLATE_GROUP}/{TEMPLATE_NAME}", load_test_data, dry_run=True)
    
    captured = capsys.readouterr()
    assert '"name": "my-node-project"' in captured.out
    assert '"express": "^4.18.2"' in captured.out

def test_mass_render(load_test_data):
    """Test rendering multiple JSON files"""
    data_list = [load_test_data] * 2  # Simulating mass rendering with 2 copies of the same data
    output_dir = "tests/mass_output"
    
    os.makedirs(output_dir, exist_ok=True)
    engine.mass_render(data_list, TEMPLATE_GROUP, output_dir=output_dir)

    # Check if the files were generated
    output_files = os.listdir(output_dir)
    assert len(output_files) == 2

def test_add_template_folder():
    """Test dynamically adding an external template folder"""
    new_template_dir = "tests/custom_templates"
    os.makedirs(new_template_dir, exist_ok=True)
    
    engine.add_template_folder(new_template_dir)
    assert new_template_dir in engine.template_dirs

