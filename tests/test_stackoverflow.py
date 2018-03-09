import unittest
import stackoverflow
import os

class TestStackoverflow(unittest.TestCase):
    def test_frameworks(self):
        # download survey if needed
        if not os.path.exists("survey2017.csv"):
            stackoverflow.downloadSurvey()

        # get list of web frameworks used by Python developers
        frameworks = stackoverflow.getFrameworksByLanguage("Python")
        print(frameworks)

        # check values are as expected
        self.assertEquals(frameworks['None'], 5544)
        self.assertEquals(frameworks['React'], 1457)
