""" Student file """

from datetime import date, timedelta
import requests


class Student:
    """A student class as base for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        """ Get the full name """
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        """ Get the email """
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def alert_santa(self):
        """ Set up the naughty behaviour """
        self.naughty_list = True

    def apply_extension(self, days):
        """ Get more time """
        self.end_date = self.end_date + timedelta(days=days)

    def course_schedule(self):
        """ Get the server """
        response = requests.get(f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"
