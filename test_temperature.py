from unittest import TestCase, main
from temperature import Temperature

class test_temperature(TestCase):
    def test_noArgs(self):
        self.assertRaises(ValueError, Temperature, None)

    def test_manyArgs(self):
        self.assertRaises(ValueError, Temperature, 5, 3)

    def test_celsius_to_kelvin(self):
        celsius = 28
        kelvin = celsius + 273.15
        self.assertEqual(Temperature(celsius=celsius).kelvin, kelvin)
    
    def test_fahrenheit_to_kelvin(self):
        fahrenheit = 28
        kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
        self.assertEqual(Temperature(fahrenheit=fahrenheit).kelvin, kelvin)

    def test_sample_kelvin(self):
        kelvin = 28
        self.assertEqual(Temperature(kelvin=kelvin).kelvin, kelvin)

    def test_negative_kelvin(self):
        kelvin = -28
        self.assertRaises(ValueError, Temperature, kelvin)

if __name__ == "__main__":
    main()