"""Just exists for now"""
from setup_class import Setup
import yaml
import os


class Settings:
    def __init__(self):
        self.setup = Setup()
        self.settings_file_path = self.setup.settings_file_path
        self.settings_file_contents = self.read_settings()

    def read_settings(self):
        with open(self.settings_file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
            return yaml_data

    def add_setting(self, key_to_add, value_to_add):
        # Read existing YAML content
        file_contents = self.read_settings()

        # Update the in-memory dictionary
        file_contents[key_to_add] = value_to_add

        # Write the updated content back to the YAML file
        with open(self.settings_file_path, 'w') as file:
            yaml.dump(file_contents, file)

if __name__ == "__main__":
    settings = Settings()
    print(settings.settings_file_contents)