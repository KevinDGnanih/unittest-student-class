""" Test file for the student file """

import unittest
from datetime import timedelta
from unittest.mock import patch
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

    def test_apply_extension(self):
        """ Check the date   """
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        """ Check if the the server work with success """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        """ Check if the server doesn't work """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")


if __name__ == '__main__':
    unittest.main()
