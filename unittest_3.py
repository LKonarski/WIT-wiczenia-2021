import unittest


def is_numeric(arg):
    return isinstance(arg, (int, float))


def is_negative(num):
    return num < 0


def calculate_savings(starting_amount, monthly_payment, monthly_deductions):
    if not is_numeric(starting_amount) or not is_numeric(monthly_payment) or not is_numeric(monthly_deductions):
        raise ValueError("All arguments must be numeric.")

    if is_negative(starting_amount) or is_negative(monthly_payment) or is_negative(monthly_deductions):
        raise ValueError("All arguments must be positive numbers.")

    return starting_amount + 12 * (monthly_payment - monthly_deductions)

class Test(unittest.TestCase):
    def test_is_numeric(self):
        self.assertTrue(is_numeric(2))
        self.assertTrue(is_numeric(2.0))
        self.assertFalse(is_numeric('dwa'))

    def test_is_negative(self):
        self.assertTrue(is_negative(-1))
        self.assertTrue(is_negative(-1.0))
        self.assertFalse(is_negative(1))
        self.assertFalse(is_negative(0))

    def test_calculate_savings(self):
        self.assertEqual(calculate_savings(1000, 1000, 200), 10600)
        self.assertNotEqual(calculate_savings(1000, 1000, 200), 10000)

unittest.main()