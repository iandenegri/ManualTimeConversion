import unittest

from time_format_conversions import determine_time_format


# No real tests yet, just trying to see if I can set up unit tests and get them to pass.
class TestMethods(unittest.TestCase):
    def setUp(self):
        self.ampm_time = "08:00 PM"
        self.military_time = "20:00"
        self.not_a_time = "Wowee"
        self.lil_uwu = "uwu"

    def test_det_time_format(self):
        self.assertEqual(determine_time_format(), "uwu")

    def test_setting_up(self):
        self.assertEqual(self.lil_uwu, "uwu")

    def test_an_actual_scenario(self):
        self.assertEqual(determine_time_format(), self.lil_uwu)


# Run the tests if this file is run directly.
if __name__ == "__main__":
    unittest.main()