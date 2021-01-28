import unittest
from employee_class import Employee


class TestEmployee(unittest.TestCase):
    """Test Employee Class."""

    def setUp(self):
        self.employee = Employee('Ravikumar', 'Shankarappa', 1200000)

    def test_give_default_raise(self):
        salary = self.employee.give_raise()
        self.assertEqual(salary, 1205000)

    def test_give_custom_raise(self):
        salary = self.employee.give_raise(1000000)
        self.assertEqual(salary, 2200000)


if __name__ == '__main__':
    unittest.main()
