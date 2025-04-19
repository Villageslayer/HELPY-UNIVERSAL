from mouse_driver.InputMethods.InputMethod import InputMethod
from typing import override
from time import sleep
import ctypes
import os

class InputMethodGFCK(InputMethod):
  NAME:str = "GFCK"
  def __init__(self):
    super().__init__()
    current_dir = os.path.dirname(__file__)
    dll_path = os.path.join(current_dir, './Lib/logitech-cve.dll')
    self.dll = ctypes.CDLL(dll_path)

  @override
  def down(self, button):
    self.dll.mouse_move(button, 0, 0, 0)

  @override
  def up(self, button):
    self.dll.mouse_move(0, 0, 0, 0)

  @override
  def click(self, button):
    self.down(button)
    sleep(0.1)
    self.up(button)

  @override
  def moveRelative(self,x,y):
    self.dll.mouse_move(0,x,y,0)

  def __call__(self, *args, **kwargs):
    """

    :param args: button,x,y,wheel
    :param kwargs:
    :return:
    """
    self.dll.mouse_move(*args)