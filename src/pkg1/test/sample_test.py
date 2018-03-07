#!/usr/bin/env python

import rospy
import rostest
import unittest


class SampleTest(unittest.TestCase):
    def runTest(self):
        rospy.sleep(3.0)
        self.assertTrue(True)


if __name__ == "__main__":
    rostest.rosrun("pkg1", "sample_test", SampleTest)

