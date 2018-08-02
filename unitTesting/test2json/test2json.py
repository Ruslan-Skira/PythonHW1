import datetime
import json

from django.conf import settings
import requests
import unittest


class MainTestCase(unittest.TestCase):
     def test_two_json(self):
         print("hi")
         self.assertGreaterEqual(3, 2)


if __name__ == '__main__':
    unittest.main()

