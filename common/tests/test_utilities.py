from freezegun import freeze_time
from time import time

from common.utilities import TimeUtils
from tests import MongoTestCase


class TimeUtilsTests(MongoTestCase):
    
    @freeze_time("2020-01-14 12:00:01")
    def setUp(self):
        super(TimeUtilsTests, self).setUp()
        self.expected_time_in_seconds = int(time())
    
    @freeze_time("2020-01-14 12:00:01")
    def test_now(self):
        self.assertEqual(TimeUtils.now(), self.expected_time_in_seconds)
    
    @freeze_time("2020-01-14 12:00:01")
    def test_time_from_seconds_with_no_param(self):
        """
        Test that with no params function uses current time.
        """
        
        calculated_value = TimeUtils.time_from_seconds()
        self.assertEqual(calculated_value.tm_year, 2020)
        self.assertEqual(calculated_value.tm_mon, 1)
        self.assertEqual(calculated_value.tm_mday, 14)
        self.assertEqual(calculated_value.tm_hour, 12)
        self.assertEqual(calculated_value.tm_min, 0)
        self.assertEqual(calculated_value.tm_sec, 1)
    
    @freeze_time("2018-11-01 3:20:11")
    def test_time_from_seconds_with_param(self):
        """
        Test that with no params function uses current time.
        """
        time_in_seconds = TimeUtils.now()
        time_in_seconds += 5
        calculated_value = TimeUtils.time_from_seconds(time_in_seconds)
        self.assertEqual(calculated_value.tm_year, 2018)
        self.assertEqual(calculated_value.tm_mon, 11)
        self.assertEqual(calculated_value.tm_mday, 1)
        self.assertEqual(calculated_value.tm_hour, 3)
        self.assertEqual(calculated_value.tm_min, 20)
        self.assertEqual(calculated_value.tm_sec, 16)
    
    @freeze_time("2020-01-14 12:00:01")
    def test_time_string_from_seconds_no_param(self):
        time_string = TimeUtils.time_string_from_seconds()
        self.assertEqual(time_string, "Tue, 14 Jan 2020 12:00:01")
    
    @freeze_time("2018-11-01 3:20:11")
    def test_time_string_from_seconds_with_param(self):
        time_in_seconds = TimeUtils.now()
        time_in_seconds += 65
        time_string = TimeUtils.time_string_from_seconds(seconds=time_in_seconds)
        self.assertEqual(time_string, "Thu, 01 Nov 2018 03:21:16")
    
    