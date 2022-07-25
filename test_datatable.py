import unittest

from domain import DataTable


class DataTableTest(unittest.TestCase):
    def test_add_column(self):
        self.AssertEqual(0, len(self.table.__columns))

        self.table.add_column('BId', 'bigint')
        self.AssertEqual(1, len(self.table.__columns))
        
        self.table.add_column('value', 'numeric')
        self.assertEqual(2, len(self.table.__columns))