import json
import unittest
from unittest import TestCase


class MainTestCase(TestCase):
    # def test_by_article(self):
    #     with open('parts_first_simple.json') as i:
    #         file = json.load(i)
    #         file_q = file['search_params']['q']
    #     with open('parts_second_simple.json') as n:
    #         response = json.load(n)
    #         result = []
    #     for k_f in file['results']:
    #         for k_r in response['results']:
    #             if k_f['article'] == k_r['article'] and k_f['brand'] == k_r['brand']:
    #                 for f_values in k_f['offers']:
    #                     for r_values in k_r['offers']:
    #                         if f_values['uuid'] == r_values['uuid']:
    #                             if f_values['price'] == r_values['price']:
    #                                 result.append(r_values)
    #                             else:
    #                                 print('from file' + str(f_values) + '\nfrom response' + str(r_values))
    #             result = []
    #             print(len(result))

    def json_filter(self):
        with open('parts_first_simple.json') as i:
            file = json.load(i)
        def lkj():
            print("hello")
        print(lkj())





