import unittest

from domain import DataTable


class DataTableTest(unittest.TestCase):
    def setUp(self):
        self.table = DataTable("A")
    
    def test_add_column(self):
        self.AssertEqual(0, len(self.table.__columns))

        self.table.add_column('BId', 'bigint')
        self.AssertEqual(1, len(self.table.__columns))
        
        self.table.add_column('value', 'numeric')
        self.assertEqual(2, len(self.table.__columns))
        
        self.table.add_column('desc','varchar')
        self.assertEqual(3, len(self.table.__columns))
    
    def test_add_column_invalid_type(self):
        a_table = DataTable('A')
        error = False
        
        try:
            a_table.add_column, ('col', 'invalid'))
        except:
            error = True
            
        if not error:
            self.fail('Chamada não gerou erro mas deveria')
            
    def test_add_relationship(self):
        a_table = DataTable('A')
        col = a_table.add_column('BId', 'bigint')
        b_table = DataTable('B')
        col = b_table.add_column(BId, 'bigint')
        b_table = add_referenced('A', a_table, col)