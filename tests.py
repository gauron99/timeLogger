#!/usr/bin/python3
import os,sys
import unittest
import timeDifference as timeDiff
from datetime import time

"""
testing file for everything i guess, atleast for now, gonna do different test and
just comment them out probably, doesn't have to be very complex, just has to work
to debug right
"""

td = timeDiff.TimeDifference()

class TestTimeDifferenceModule(unittest.TestCase):

    def test_easy_under_minute(self):
        "first test try"
        # td = timeDiff.TimeDifference()
        self.assertEqual('less than a minute',td.timeAprox(time(0,0,1)))
        self.assertEqual('less than a minute',td.timeAprox(time(0,0,20)))
        self.assertEqual('less than a minute',td.timeAprox(time(0,0,59)))

    def test_easy_around_5_mins(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 5 mins',td.timeAprox(time(0,1,0)))
        self.assertEqual('around 5 mins',td.timeAprox(time(0,2,35)))
        self.assertEqual('around 5 mins',td.timeAprox(time(0,5,19)))
        self.assertEqual('around 5 mins',td.timeAprox(time(0,7,19)))
        self.assertEqual('around 5 mins',td.timeAprox(time(0,9,59)))

    def test_easy_around_15_mins(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 15 mins',td.timeAprox(time(0,10,00)))
        self.assertEqual('around 15 mins',td.timeAprox(time(0,19,59)))
        self.assertEqual('around 15 mins',td.timeAprox(time(0,15,19)))
        self.assertEqual('around 15 mins',td.timeAprox(time(0,22,29)))
    
    def test_easy_around_30_mins(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 30 mins',td.timeAprox(time(0,22,30)))
        self.assertEqual('around 30 mins',td.timeAprox(time(0,30,00)))
        self.assertEqual('around 30 mins',td.timeAprox(time(0,40,49)))
        self.assertEqual('around 30 mins',td.timeAprox(time(0,44,59,999999)))
        
    def test_easy_around_one_hour(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around an hour',td.timeAprox(time(0,45,00)))
        self.assertEqual('around an hour',td.timeAprox(time(1,0,9)))
        self.assertEqual('around an hour',td.timeAprox(time(1,9,59)))
        self.assertEqual('around an hour',td.timeAprox(time(1,14,59)))

    def test_easy_around_one_hour_30_mins(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around hour and 30 mins',td.timeAprox(time(1,15,0)))
        self.assertEqual('around hour and 30 mins',td.timeAprox(time(1,20,19)))
        self.assertEqual('around hour and 30 mins',td.timeAprox(time(1,35,5)))
        self.assertEqual('around hour and 30 mins',td.timeAprox(time(1,44,59)))



if __name__ == "__main__":
    unittest.main()