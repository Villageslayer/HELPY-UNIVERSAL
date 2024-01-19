# recoil_calc.py
from weapon_loader import WeaponLoader

class RecoilCalculator:
    def __init__(self):
        self.weapon_loader = WeaponLoader()
        self.weapon_names = self.weapon_loader.get_all_weapon_names()
        self.rpm_values = self.weapon_loader.get_all_rpm_values()
        self.timings = self.calculate_timings_per_weapon()

    def calculate_timing_for_weapon(self, rpm):
        """Calculate timing in milliseconds for a given RPM using the formula."""
        # Using the given formula: 60000 / ((n - 1) / t ± 16.7)
        # Here, n = 60000 and t = rpm
        return round(6000 / rpm)  # Using the formula to calculate timing

    def calculate_timings_per_weapon(self):
        """Calculate timings for each weapon based on RPM."""
        timings = []
        for rpm in self.rpm_values:
            timing = self.calculate_timing_for_weapon(rpm)
            timings.append(timing)
        return timings

    def get_timings(self):
        """Return calculated timings for each weapon."""
        return self.timings

    def get_weapon_data(self):
        """Return weapon names, RPM values, and calculated timings."""
        return zip(self.weapon_names, self.rpm_values, self.timings)


if __name__ == "__main__":
    from weapon_loader import WeaponLoader

    # Create an instance of the WeaponLoader class
    weapon_loader = WeaponLoader()

    # Create an instance of the RecoilCalculator class
    calculator = RecoilCalculator(weapon_loader)

    # Get and print weapon data with names, RPM values, and calculated timings
    for name, rpm, timing in calculator.get_weapon_data():
        print(f"Weapon Name: {name}, RPM: {rpm}, Timing: {timing:.2f} milliseconds")
