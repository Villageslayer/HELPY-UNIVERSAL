class CursorMovementCalculator:
    def __init__(self):
        """
        Initialize the CursorMovementCalculator with default settings.
        """
        self.sensitivity = 6
        self.movement = 3

    def calculate_cursor_movement(self, new_sensitivity, dpi):
        """
        Calculate cursor movement based on the sensitivity and DPI settings.

        Args:
        - new_sensitivity (int): New sensitivity setting.
        - dpi (int): Dots per inch setting of the mouse or device.

        Returns:
        - int: Calculated cursor movement rounded to the nearest integer.
        """
        k = (self.sensitivity * self.movement) / dpi
        cursor_movement = (k * dpi) / new_sensitivity
        return round(cursor_movement)


if __name__ == "__main__":
    # Create an instance of the CursorMovementCalculator class
    calculator = CursorMovementCalculator()

    # Taking new_sensitivity and DPI as user input
    new_sensitivity = int(input("Enter the new sensitivity setting: "))
    dpi = int(input("Enter the DPI setting of your mouse"))

    # Calculate cursor movement for the given sensitivity and DPI using the class method
    new_movement = calculator.calculate_cursor_movement(new_sensitivity, dpi)

    # Output the result
    print(
        f"For sensitivity {new_sensitivity} and DPI {dpi}, move the cursor approximately {new_movement} pixels every to cancel recoil"
    )
