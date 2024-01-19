# weapon_loader.py

import os
import yaml


class WeaponLoader:
    def __init__(self, dir_path='.\\yaml\\'):
        self.dir_path = dir_path
        self.file_names = ['AR.yaml', 'SMG.yaml', 'MP.yaml', 'LMG.yaml']
        self.all_weapon_names = []
        self.all_rpm_values = []

        self.load_and_process_files()

    def load_yaml_file(self, file_path):
        """Load data from a YAML file."""
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data

    def extract_weapon_data(self, data):
        """Extract weapon names and RPM values."""
        weapon_names = []
        rpm_values = []

        for weapon_type, weapons in data.items():
            for weapon_name, rpm in weapons.items():
                weapon_names.append(weapon_name)
                rpm_values.append(rpm)

        return weapon_names, rpm_values

    def load_and_process_files(self):
        """Load and process all YAML files."""
        for file_name in self.file_names:
            file_path = os.path.join(self.dir_path, file_name)

            if os.path.exists(file_path):
                data = self.load_yaml_file(file_path)

                weapon_names, rpm_values = self.extract_weapon_data(data)

                self.all_weapon_names.extend(weapon_names)
                self.all_rpm_values.extend(rpm_values)

                self.print_weapon_data(file_name, weapon_names, rpm_values)
            else:
                print(f"The file {file_name} does not exist.")

    def print_weapon_data(self, file_name, weapon_names, rpm_values):
        """Print weapon names and RPM values."""
        print(f"Weapon names from {file_name}: {weapon_names}")
        print(f"RPM values from {file_name}: {rpm_values}")
        print("-" * 50)  # Add separator between files

    def get_all_weapon_names(self):
        """Return all weapon names."""
        return self.all_weapon_names

    def get_all_rpm_values(self):
        """Return all RPM values."""
        return self.all_rpm_values
