import unittest
import pandas as pd
import fitz
from readexcel import ReadExcel
from BHMG.rename import Rename


class TestExcelMethods(unittest.TestCase):
    def test_hello():
        self.assertEqual('test', 'test')


if __name__ == '__main__':
    unittest.main()
