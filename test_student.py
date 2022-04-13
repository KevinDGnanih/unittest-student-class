""" Test file for the student file """

import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """ Class for the Student test """

    @classmethod
    def setUpClass(cls):
        """ Thise method make setUpClass start at
        the beginning of the file test"""
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        """ This method make tearDownClass start at
        the end of the test file """
        print('tearDownclass')

    def setUp(self):
        """ This method make the setUp start before each test """
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        """ This method make the teardown start after each test """
        print('tearDown')

    def test_full_name(self):
        """ Get the full name test """
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        """ get the naughty check """
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        """ Check the email with the full name  """
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')


if __name__ == '__main__':
    unittest.main()
