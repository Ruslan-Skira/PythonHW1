import unittest
import json



class Mainunittest(unittest.TestCase):
    def test_greater_then(self):
        with open('/Users/ruslanskira/PycharmProjects/HW1/APITesting/vesna_testing/parts_first.json') as f:
            first = json.load(f)
        first_number = first["num_of_products"]
        with open('/Users/ruslanskira/PycharmProjects/HW1/APITesting/vesna_testing/parts_second.json') as s:
            second = json.load(s)
        second_number = second["num_of_products"]

        self.assertGreaterEqual( second_number, first_number)
