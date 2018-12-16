#!/usr/bin/env python

import rospy
import sys

if __name__ == '__main__':
    rospy.init_node('print_arg')
    rospy.logerr(sys.argv)
    print(sys.argv)
