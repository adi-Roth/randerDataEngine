# randerDataEngine
randerDataEngine (RDE) is a flexible and powerful template rendering engine built upon Jinja2. It allows users to dynamically generate files and projects by rendering templates with provided JSON data. RDE supports adding external template directories, rendering single or multiple JSON data files, and includes a dry-run mode for previewing outputs.

# Features
- **Dynamic Template Management:** Easily add external template directories without altering existing ones.
- **Single and Mass Rendering:** Render files using individual JSON data or perform batch rendering with multiple JSON files.
- **Dry-Run Mode:** Preview rendered outputs in the console before saving them.
- **Default Templates:** Comes with built-in templates for Dockerfiles, Node.js projects (with support for unit tests, API tests, coverage collection, TypeScript, and linting), Angular projects, and Python projects.

# Installation
Install RDE using pip:
``` python
pip install randerDataEngine
```

# Usage
## Initialization
Begin by importing and initializing the `RanderDataEngine`:
``` python
from randerDataEngine import RanderDataEngine

# Initialize the engine
engine = RanderDataEngine()
```

## Adding External Template Folders
To include additional template directories:
``` python
engine.add_template_folder('path/to/your/templates')
```

## Rendering a Single Template
Render a specific template with your JSON data:
``` python
import json

# Load your JSON data
with open('path/to/your/data.json') as f:
    data = json.load(f)

# Render the template
output = engine.render_template('template_name.j2', data)

# Save the output to a file
with open('output_file.txt', 'w') as f:
    f.write(output)
```

## Rendering a Group of Templates
Render all templates within a specific folder:
``` python
# Render all templates in the 'nodejs' template group
engine.render_group('nodejs', data, output_dir='path/to/output/directory')
```

## Mass Rendering with Multiple JSON Files
Render templates using multiple JSON data files:
``` python
import json

# List of JSON data files
data_files = ['data1.json', 'data2.json']

# Load JSON data
data_list = []
for file in data_files:
    with open(file) as f:
        data_list.append(json.load(f))

# Perform mass rendering
engine.mass_render(data_list, 'nodejs', output_dir='path/to/output/directory')
```

## Dry-Run Mode
Preview the rendered output without saving:
``` python
engine.render_template('template_name.j2', data, dry_run=True)
```

# Default Templates
RDE includes the following default templates:
- **Dockerfile Template:** Located in templates/docker/Dockerfile.j2.
- **Node.js Project Template:** Located in templates/nodejs/. Supports unit tests, API tests, coverage collection, TypeScript, and linting.
- **Angular Project Template:** Located in templates/angular/.
- **Python Project Template:** Located in templates/python/.

# Module Structure
``` bash
randerDataEngine/                  # Main package
│── templates/                      # Default templates directory
│   ├── docker/                     # Dockerfile templates
│   │   ├── Dockerfile.j2
│   ├── nodejs/                     # Node.js project template
│   │   ├── package.json.j2
│   │   ├── tsconfig.json.j2
│   │   ├── jest.config.js.j2
│   │   ├── Dockerfile.j2
│   ├── angular/                    # Angular project template
│   │   ├── package.json.j2
│   │   ├── angular.json.j2
│   │   ├── tsconfig.json.j2
│   │   ├── Dockerfile.j2
│   ├── python/                     # Python project template
│   │   ├── setup.py.j2
│   │   ├── requirements.txt.j2
│   │   ├── main.py.j2
│── rde.py                           # Main module logic
│── __init__.py                      # Package initialization
│── config.py                        # Configurations
│── utils.py                         # Helper functions
│── README.md                        # Documentation
│── setup.py                         # PyPI packaging
│── tests/                           # Unit tests
│   ├── test_rde.py
│── examples/                        # Example templates & data
│   ├── example.json
│   ├── example_node.json
│   ├── example_python.json
```

# Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
