from nicegui import ui
from setup_class import Setup
from settings_class import Settings
import yaml


class SetupUI:
    def __init__(self):
        self.setup = Setup()
        self.settings = Settings()
        self.dpi = 0
        self.dpi_input_field = None

    def dpi_input(self):
        self.dpi_input_field = ui.number(label="DPI", on_change=print(self.dpi))
        self.dpi = self.dpi_input_field.value
        print(self.dpi)
        continue_button = ui.button('continue',on_click=self.dpi_continue())

    def dpi_continue(self):
        print(self.dpi)

    def run(self):
        ui.run(native=True, frameless=True, title='Recoil Setup', dark=True)
if __name__ in ("__main__", "__mp_main__"):
    setupui = SetupUI()
    setupui.dpi_input()
    setupui.run()

