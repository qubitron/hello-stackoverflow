import unittest
import stackoverflow
import os

class TestStackoverflow(unittest.TestCase):
    def test_language_2017(self):
        # get list of web frameworks used by Python developers
        languages = stackoverflow.languages_breakdown(2017).to_dict()

        self.assertAlmostEqual(languages['percent']['Java'], 39.7, 1)
        self.assertAlmostEqual(languages['percent']['C#'], 34.1, 1)
        self.assertAlmostEqual(languages['percent']['Python'], 32.0, 1)
        self.assertAlmostEqual(languages['percent']['C++'], 22.3, 1)

    # def test_language_percents(self):
    #     # get list of web frameworks used by Python developers
    #     languages = stackoverflow.languages_breakdown(2015).to_dict()

    #     self.assertAlmostEqual(languages['percent']['Java'], 37.4, 1)
    #     self.assertAlmostEqual(languages['percent']['C#'], 31.6, 1)
    #     self.assertAlmostEqual(languages['percent']['Python'], 23.8, 1)
    #     self.assertAlmostEqual(languages['percent']['C++'], 20.6, 1)
        
        

