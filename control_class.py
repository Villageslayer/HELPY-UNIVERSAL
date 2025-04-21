from mouse_driver.InputMethods.InputMethodGFCK import InputMethodGFCK
from threading import Thread
from win32api import GetKeyState
from time import sleep


class Control(Thread):
    name = 'Control'  # used for logging
    MouseInput=InputMethodGFCK()
    def __init__(self):
        super(Control, self).__init__()

        self.stop = False
        self.running = False
        self.active = False
        self.move_x = 0
        self.move_y = 0
        self.timing = 0
        self.r_mouse = 0x02
        self.l_mouse = 0x01
        self.move_click = True

    def run(self, name=name):
        """The main loop"""
        self.running = True  #
        while self.running:
            self.check_status()
            if self.active:
                if not self.move_click:
                    self.movement()
                    continue
                self.movement_with_click()
                continue

            sleep(0.1)

    def check_status(self):
        """Checks if both mouse buttons are pressed"""
        if GetKeyState(self.r_mouse) < 0 and GetKeyState(self.l_mouse) < 0:
            self.active = True
        else:
            self.active = False

    def cleanup(self):
        """call this to stop main Loop"""
        self.running = False
        self.join()

    def reset(self):
        """"Stopping to update Values (x,y,t)"""
        self.stop = True
        self.move_x, self.move_y, self.timing = 0, 0, 0

    def update(self, x, y, t, move_click):
        """ Update Recoil Values
            input (x,y,t)
        """
        self.reset()
        self.move_x, self.move_y, self.timing,self.move_click = x, y, (t * 0.001) , move_click # convert seconds to milliseconds
        self.stop = False

    def current(self, debug=False):
        """prints current Value for debug / logging
        input printout True to print
        """
        if debug:
            print(f'current values: {self.move_x, self.move_y, self.timing}')
        return self.move_x, self.move_y, self.timing

    def movement(self):
        if not self.stop:
            self.MouseInput.moveRelative(self.move_x, self.move_y) # move the mouse
            sleep(self.timing)  # sleep for t milliseconds

    def movement_with_click(self):
        if not self.stop:
            self.MouseInput.up(1)
            self.MouseInput.moveRelative(self.move_x, self.move_y)  # move the mouse
            sleep(self.timing)  # sleep for t milliseconds
            self.MouseInput.down(1)

if __name__ == "__main__":
    import keyboard
    con = Control()
    con.start()
    con.update(0, 5, 6)
    con.current(debug=True)
    def stop():
        con.cleanup()
    def update():
        con.update(0, 3, 8)
        con.current(debug=True)
    keyboard.add_hotkey("F10", stop, suppress=True)
    keyboard.add_hotkey("F9", update, suppress=True)
    con.run(name=Control)
