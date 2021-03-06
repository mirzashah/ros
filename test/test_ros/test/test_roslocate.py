#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id: test_embed_msg.py 1986 2008-08-26 23:57:56Z sfkwc $

PKG = 'test_ros'
NAME = 'test_roslocate'
import roslib; roslib.load_manifest(PKG)
import sys
import unittest
import rostest
import subprocess
import os

class RoslocateTestCase(unittest.TestCase):
    def go(self, cmd, pkg=None):
        roslocate = os.path.join(os.environ['ROS_ROOT'],'bin','roslocate')
        command = [roslocate, cmd]
        if pkg:
            command.append(pkg)
        try:
	    # I don't understand why, but on OSX, calling 'roslocate list'
	    # via subprocess.check_call() hangs if stdout is redirected to
	    # a PIPE.  If it's not redirected, then it doesn't hang.
	    if 'Darwin' in os.uname() and cmd == 'list':
              subprocess.check_call(command, stderr=subprocess.PIPE)
	    else:
              subprocess.check_call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except subprocess.CalledProcessError:
            return False

    def testDescribe(self):
        self.assertTrue(self.go('describe', 'roscpp'))

    def testSvn(self):
        self.assertTrue(self.go('svn', 'roscpp'))

    def testRepo(self):
        self.assertTrue(self.go('repo', 'roscpp'))

    def testSearch(self):
        self.assertTrue(self.go('search', 'roscpp'))

    def testList(self):
        self.assertTrue(self.go('list'))

    def testInvalidCommand(self):
        self.assertFalse(self.go('foo', 'roscpp'))

if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, RoslocateTestCase, sys.argv)
