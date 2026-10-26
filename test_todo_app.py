import unittest
from todo_app import isOverdue

class TestTodoApp(unittest.TestCase):
    def test_not_overdue(self):
        self.assertFalse(isOverdue('2023-01-20', '2023-01-14'))

    def test_overdue(self):
        self.assertTrue(isOverdue('2023-01-10', '2023-01-14'))

if __name__ == '__main__':
    unittest.main()