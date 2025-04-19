from InputMethods.InputMethod import InputMethod
from time import sleep

#Here for Example
class ExampleMouseInput:
  def __init__(self):
    ...
  def mouse_down(self,button):
    ...
  def mouse_up(self,button):
    ...
  def mouse_move(self,x,y):
    ...
  ...

class InputMethodExample:
  NAME: str = "Example"

  def __init__(self):
    self.exampleInput = ExampleMouseInput()
    ...

  def down(self, button):
    self.exampleInput.mouse_down(button)
    ...

  def up(self, button):
    self.exampleInput.mouse_up(button)
    ...

  def click(self, button):
    self.down(button) # Down
    sleep(0.1) # Delay
    self.up(button) # up
    ...

  def moveRelative(self, x, y):
    self.exampleInput.mouse_move(x,y)
    ...