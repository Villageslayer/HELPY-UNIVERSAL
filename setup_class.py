import os
import glob
import configparser
from calculator_class import CursorMovementCalculator
import yaml


class Setup:
    """Used for initial setup
    gets the Sensitivity from R6 Game settings file
     also contains the recoil calculator for simplicity / because its part of the setup"""

    def __init__(self, debug=False):
        self.debug = debug
        self.sensitivity_x, self.sensitivity_y = 0, 0
        self.sensitivity = 0
        self.recoil_x_value = 0
        self.dpi = 0
        self.user_document_folder = self.get_user_document_folder()
        self.config_location = self.get_game_settings_file()
        self.first_launch, self.settings_file_path = self.check_first_launch()

    def check_first_launch(self):
        """Check for first launch by checking if settings.yaml is present"""
        script_directory = os.path.dirname(os.path.abspath(__file__))  # get cwd / script location
        file_name = 'settings.yaml'
        file_path = os.path.join(script_directory, file_name)
        if os.path.exists(file_path):
            return False, file_path
        else:
            self.dpi = int(input('please input your DPI:'))
            self.simplify_sensitivity()
            data = {"first_launch": False,
                    'DPI': self.dpi,
                    'recoil_x': self.recoil_x_value,
                    'timings': [8, 8, 8]}

            with open(file_path, 'w') as new_file:
                yaml.dump(data, new_file, default_flow_style=False)
                return True, file_path

    def simplify_sensitivity(self):
        """if x and y are equal return x else return both"""
        self.get_mouse_sensitivity_settings()
        self.calculate_recoil_value()
        if self.sensitivity_y == self.sensitivity_x:
            self.sensitivity = self.sensitivity_x
            return self.sensitivity
        else:
            return (self.sensitivity_x, self.sensitivity_y)

    @staticmethod
    def get_user_document_folder():
        """Get location of Documents"""
        home_dir = os.path.expanduser("~")
        document_folder = os.path.join(home_dir, 'Documents')
        return document_folder

    def get_game_settings_file(self):
        """this is where we find the path for GameSettings.ini """
        r6s_settings_path = os.path.join(self.user_document_folder, 'My Games', 'Rainbow Six - Siege')  # construct path
        ini_files = glob.glob(os.path.join(r6s_settings_path, '*', 'GameSettings.ini'))  # find ini File/files
        if not ini_files:  # return early if none found
            return None
        else:  # return files
            latest_ini = max(ini_files, key=os.path.getmtime)  # if multiple take latest
            return latest_ini

    def debug_logging(self):
        """debugging print"""
        if not self.debug:  # early return if not in debug mode
            return
        else:  # debug output
            print(f"Location:{self.config_location}\nSensitivity:{self.sensitivity}\nFirst Launch: \
        {self.first_launch}\nSettings path:{self.settings_file_path}\n {self.sensitivity_x, self.sensitivity_y}\n\
{self.recoil_x_value}")
            # os.remove(self.settings_file_path) dev tool to remove the config

    def get_mouse_sensitivity_settings(self):
        """Use Configparser to Get the values
         for MouseYawSensitivity and MousePitchSensitivity"""
        config = configparser.ConfigParser()  # innit configparser
        config.read(self.config_location)
        # Get the values for MouseYawSensitivity and MousePitchSensitivity as integers
        self.sensitivity_y = config.getint('INPUT', 'MouseYawSensitivity', fallback=None)
        self.sensitivity_x = config.getint('INPUT', 'MousePitchSensitivity', fallback=None)

    def calculate_recoil_value(self):
        """just here because it's part of the setup needs user DPI input """
        calculator = CursorMovementCalculator()
        recoil_x = calculator.calculate_cursor_movement(new_sensitivity=self.sensitivity_x, dpi=self.dpi)
        self.recoil_x_value = recoil_x


if __name__ == "__main__":
    setup = Setup(debug=True)
    setup.debug_logging()
