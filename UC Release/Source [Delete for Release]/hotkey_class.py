import keyboard as kb
from settings_class import Settings
from control_class import Control

class Hotkeys:
    def __init__(self):
        self.settings = Settings()
        self.control = Control()
        self.settings_content = self.settings.settings_file_contents
        self.timings = self.settings_content['timings']
        self.recoil_low = self.settings_content['recoil_x']
        self.recoil_medium = round(self.recoil_low * 1.6)
        self.recoil_high = round(self.recoil_low * 2.3)
        self.low_key = "F5"
        self.medium_key = "F6"
        self.high_key = "F7"
        self.add_hotkeys()

    def add_hotkeys(self):
        kb.add_hotkey(str(self.low_key),self.F5, suppress=True )
        kb.add_hotkey(str(self.medium_key), self.F6, suppress=True )
        kb.add_hotkey(str(self.high_key), self.F7, suppress=True )

    def F5(self):
        self.control.update(0, self.recoil_low, self.timings[0])
    def F6(self):
        self.control.update(0, self.recoil_medium, self.timings[1])
    def F7(self):
        self.control.update(0, self.recoil_high, self.timings[2])

if __name__ == "__main__":
    hk = Hotkeys()
    #print(hk.timings,hk.recoil_low,hk.recoil_medium, hk.recoil_high )
    hk.control.run(name='UC FREE RELEASE')
    kb.wait("F10")