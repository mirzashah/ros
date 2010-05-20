# Software License Agreement (BSD License)
#
# Copyright (c) 2009, Willow Garage, Inc.
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
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICTS
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

PKG = 'rxbag'
import roslib; roslib.load_manifest(PKG)

import time

def stamp_to_str(t): return time.strftime('%b %d %Y %H:%M:%S', time.localtime(t.to_sec())) + '.%03d' % (t.nsecs / 1000000)

def get_topics(bag): return sorted(set([c.topic for c in bag._get_connections()]))

def get_start_stamp(bag):
    start_stamp = None
    for connection_start_stamp in [index[0].time for index in bag._connection_indexes.values()]:
        if not start_stamp or connection_start_stamp < start_stamp:
            start_stamp = connection_start_stamp
    return start_stamp

def get_end_stamp(bag):
    end_stamp = None
    for connection_end_stamp in [index[-1].time for index in bag._connection_indexes.values()]:
        if not end_stamp or connection_end_stamp < end_stamp:
            end_stamp = connection_end_stamp
    return end_stamp

def get_topics_by_datatype(bag):
    topics_by_datatype = {}
    for c in bag._get_connections():
        topics_by_datatype.setdefault(c.datatype, []).append(c.topic)
    return topics_by_datatype

def get_datatype(bag, topic):
    for c in bag._get_connections(topic):
        return c.datatype
    return None