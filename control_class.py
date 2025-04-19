from mouse_driver.MouseMove import mouse_move as ghub_mouse
import win32api
from time import sleep


class Control:
    name = 'Control'  # used for logging

    def __init__(self):
        self.stop = False
        self.running = False
        self.active = False
        self.move_x = 0
        self.move_y = 0
        self.timing = 0
        self.r_mouse = 0x02
        self.l_mouse = 0x01

    def run(self, name):
        """The main loop"""
        self.running = True  #
        while self.running:
            self.check_status()
            if self.active and not self.stop:
                self.movement()
                continue
            sleep(0.1)

    def check_status(self):
        """Checks if both mouse buttons are pressed"""
        if win32api.GetKeyState(self.r_mouse) < 0 and win32api.GetKeyState(self.l_mouse) < 0:
            self.active = True
        else:
            self.active = False

    def cleanup(self):
        """call this to stop main Loop"""
        self.running = False

    def reset(self):
        """"Stopping to update Values (x,y,t)"""
        self.stop = True
        self.move_x, self.move_y, self.timing = 0, 0, 0

    def update(self, x, y, t):
        """ Update Recoil Values
            input (x,y,t)
        """
        self.reset()
        self.move_x, self.move_y, self.timing = x, y, t
        self.stop = False

    def current(self, debug=False):
        """prints current Value for debug / logging
        input printout True to print
        """
        if debug:
            print(f'current values: {self.move_x, self.move_y, self.timing}')
        return self.move_x, self.move_y, self.timing

    def movement(self):
        timing = self.timing * 0.001 # convert seconds to milliseconds
        ghub_mouse(self.move_x, self.move_y) # move the mouse
        sleep(timing)  # sleep for t milliseconds


if __name__ == "__main__":
    import keyboard
    con = Control()
    con.update(0, 5, 8)
    con.current(debug=True)
    def stop():
        con.cleanup()
    def update():
        con.update(0, 3, 8)
        con.current(debug=True)
    keyboard.add_hotkey("F10", stop, suppress=True)
    keyboard.add_hotkey("F9", update, suppress=True)
    con.run(name=Control)
