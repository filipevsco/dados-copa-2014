import unittest

from domain import DataTable


class DataTableTest(unittest.TestCase):
    def test_add_column(self):
        self.AssertEqual(0, len(self.table.__columns))
