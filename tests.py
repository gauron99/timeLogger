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
        "first easy tests, nothing crazy"
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

    def test_easy_around_two_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 2 hours',td.timeAprox(time(1,45,0)))
        self.assertEqual('around 2 hours',td.timeAprox(time(1,59,44)))
        self.assertEqual('around 2 hours',td.timeAprox(time(2,15,17)))
        self.assertEqual('around 2 hours',td.timeAprox(time(2,29,59)))

    def test_easy_around_3_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 3 hours',td.timeAprox(time(2,45,0)))
        self.assertEqual('around 3 hours',td.timeAprox(time(3,0,0)))
        self.assertEqual('around 3 hours',td.timeAprox(time(3,15,48)))
        self.assertEqual('around 3 hours',td.timeAprox(time(3,29,59)))

    def test_easy_around_4_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 4 hours',td.timeAprox(time(3,30,0)))
        self.assertEqual('around 4 hours',td.timeAprox(time(4,0,0)))
        self.assertEqual('around 4 hours',td.timeAprox(time(4,15,49)))
        self.assertEqual('around 4 hours',td.timeAprox(time(4,29,59)))

    def test_easy_around_5_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 5 hours',td.timeAprox(time(4,30,0)))
        self.assertEqual('around 5 hours',td.timeAprox(time(5,0,0)))
        self.assertEqual('around 5 hours',td.timeAprox(time(5,15,49)))
        self.assertEqual('around 5 hours',td.timeAprox(time(5,29,59)))


    def test_easy_around_6_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 6 hours',td.timeAprox(time(5,30,0)))
        self.assertEqual('around 6 hours',td.timeAprox(time(6,0,0)))
        self.assertEqual('around 6 hours',td.timeAprox(time(6,14,47)))
        self.assertEqual('around 6 hours',td.timeAprox(time(6,29,59)))

    def test_easy_around_7_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 7 hours',td.timeAprox(time(6,30,0)))
        self.assertEqual('around 7 hours',td.timeAprox(time(7,0,0)))
        self.assertEqual('around 7 hours',td.timeAprox(time(7,10,40)))
        self.assertEqual('around 7 hours',td.timeAprox(time(7,29,59)))

    def test_easy_around_8_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 8 hours',td.timeAprox(time(7,30,0)))
        self.assertEqual('around 8 hours',td.timeAprox(time(8,0,0)))
        self.assertEqual('around 8 hours',td.timeAprox(time(8,17,28)))
        self.assertEqual('around 8 hours',td.timeAprox(time(8,29,59)))

    def test_easy_around_9_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 9 hours',td.timeAprox(time(8,30,0)))
        self.assertEqual('around 9 hours',td.timeAprox(time(9,0,0)))
        self.assertEqual('around 9 hours',td.timeAprox(time(9,21,49)))
        self.assertEqual('around 9 hours',td.timeAprox(time(9,29,59)))

    def test_easy_around_10_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 10 hours',td.timeAprox(time(9,30,0)))
        self.assertEqual('around 10 hours',td.timeAprox(time(10,0,0)))
        self.assertEqual('around 10 hours',td.timeAprox(time(11,45,19)))
        self.assertEqual('around 10 hours',td.timeAprox(time(12,29,59)))

    def test_easy_around_15_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 15 hours',td.timeAprox(time(12,30,0)))
        self.assertEqual('around 15 hours',td.timeAprox(time(14,59,59)))
        self.assertEqual('around 15 hours',td.timeAprox(time(15,0,0)))
        self.assertEqual('around 15 hours',td.timeAprox(time(17,29,59)))

    def test_easy_around_20_hours(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('around 20 hours',td.timeAprox(time(17,30,0)))
        self.assertEqual('around 20 hours',td.timeAprox(time(19,59,40)))
        self.assertEqual('around 20 hours',td.timeAprox(time(20,20,20)))
        self.assertEqual('around 20 hours',td.timeAprox(time(21,59,59)))

    def test_easy_almost_a_day(self):
        # td = timeDiff.TimeDifference()
        self.assertEqual('almost a whole day, damn',td.timeAprox(time(22,0,0)))
        self.assertEqual('almost a whole day, damn',td.timeAprox(time(23,45,19)))
        self.assertEqual('almost a whole day, damn',td.timeAprox(time(23,59,59)))

# is it even possible to make this one? (.time method is limited to 0..23 hrs)
    # def test_easy_over_a_day(self):
    #     # td = timeDiff.TimeDifference()
    #     self.assertEqual('more than a day -- chill bro',td.timeAprox(time(25,0,0)))
    #     self.assertEqual('more than a day -- chill bro',td.timeAprox(time(,,)))
    #     self.assertEqual('more than a day -- chill bro',td.timeAprox(time(,,)))
    #     self.assertEqual('more than a day -- chill bro',td.timeAprox(time(,,)))

if __name__ == "__main__":
    unittest.main()