import os
import json
import jinja2
from typing import List, Dict

class RanderDataEngine:
    def __init__(self, default_template_dir="templates"):
        """Initialize the engine with a default template directory."""
        self.template_dirs = [default_template_dir]  
        self.env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.template_dirs))

    def add_template_folder(self, folder_path: str):
        """Dynamically add external template folders."""
        if os.path.exists(folder_path):
            self.template_dirs.append(folder_path)
            self.env.loader = jinja2.FileSystemLoader(self.template_dirs)
        else:
            raise FileNotFoundError(f"Template folder '{folder_path}' not found.")

    def render_template(self, template_name: str, data: Dict, dry_run: bool = False) -> str:
        """Render a single template with provided data."""
        try:
            template = self.env.get_template(template_name)
            result = template.render(data)
            
            if dry_run:
                print(f"\n=== Dry Run: {template_name} ===\n")
                print(result)
            
            return result
        except jinja2.TemplateNotFound:
            raise ValueError(f"Template '{template_name}' not found in loaded directories.")

    def render_group(self, template_folder: str, data: Dict, output_dir: str = None, dry_run: bool = False):
        """Render a group of templates inside a folder."""
        folder_path = os.path.join(self.template_dirs[0], template_folder)

        if not os.path.exists(folder_path):
            raise ValueError(f"Template group '{template_folder}' not found.")
        
        for file in os.listdir(folder_path):
            if file.endswith(".j2"):
                template_name = f"{template_folder}/{file}"
                rendered_content = self.render_template(template_name, data, dry_run)

                if not dry_run and output_dir:
                    os.makedirs(output_dir, exist_ok=True)
                    output_file = os.path.join(output_dir, file.replace(".j2", ""))
                    with open(output_file, "w") as f:
                        f.write(rendered_content)
    
    def mass_render(self, data_list: List[Dict], template_folder: str, output_dir: str = None, dry_run: bool = False):
        """Perform mass rendering for multiple data JSONs."""
        for i, data in enumerate(data_list):
            print(f"\n🚀 Rendering dataset {i + 1}")
            self.render_group(template_folder, data, output_dir, dry_run)
