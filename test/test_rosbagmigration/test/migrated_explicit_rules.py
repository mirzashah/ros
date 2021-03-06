class update_test_rosbagmigration_MigratedExplicit_c7936d50a749a1f589d6fc81eae24b34(MessageUpdateRule):
	old_type = "test_rosbagmigration/MigratedExplicit"
	new_type = "test_rosbagmigration/MigratedExplicit"
	old_full_text = """
Header  header
int32   field1 #17
float32 field2 #58.2
string  field3 #"aldfkja"
================================================================================
MSG: roslib/Header
#Standard metadata for higher-level flow data types
#sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
	new_full_text = """
Header  header
int32   field1 #17
float32 field2 #58.2
string  field3 #"aldfkja"
int32   field4 #82
================================================================================
MSG: roslib/Header
#Standard metadata for higher-level flow data types
#sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""

        order = 0

	migrated_types = [
		("Header","Header"),
	]

	valid = True

	def update(self, old_msg, new_msg):
		self.migrate(old_msg.header, new_msg.header)
		new_msg.field1 = old_msg.field1
		new_msg.field2 = old_msg.field2
		new_msg.field3 = old_msg.field3
		new_msg.field4 = 82



class update_test_rosbagmigration_MigratedExplicit_fa072fb3cfcf105e1e5609a7467e2a14(MessageUpdateRule):
	old_type = "test_rosbagmigration/MigratedExplicit"
	new_type = "test_rosbagmigration/MigratedExplicit"
	old_full_text = """
Header  header
int32   field1 #17
float32 field2 #58.2
string  field3 #"aldfkja"
int32   field4 #82
================================================================================
MSG: roslib/Header
#Standard metadata for higher-level flow data types
#sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
	new_full_text = """
Header  header
int32   afield1 #17
float32 afield2 #58.2
string  afield3 #"aldfkja"
int32   afield4 #82
================================================================================
MSG: roslib/Header
#Standard metadata for higher-level flow data types
#sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
        order = 1

	migrated_types = [
		("Header","Header"),
	]

	valid = True

	def update(self, old_msg, new_msg):
		self.migrate(old_msg.header, new_msg.header)
		new_msg.afield1 = old_msg.field1
		new_msg.afield2 = old_msg.field2
		new_msg.afield3 = old_msg.field3
		new_msg.afield4 = old_msg.field4


class update_test_rosbagmigration_MigratedExplicit_0a3e03fbb60b5f9abd4beedae6080fce(MessageUpdateRule):
	old_type = "test_rosbagmigration/MigratedExplicit"
	new_type = "test_rosbagmigration/MigratedExplicit"
	old_full_text = """
Header  header
int32   afield1 #17
float32 afield2 #58.2
string  afield3 #"aldfkja"
int32   afield4 #82
================================================================================
MSG: roslib/Header
#Standard metadata for higher-level flow data types
#sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
	new_full_text = """
Header  header
float32 afield2 #58.2
string  combo_field3 #"aldfkja 17"
int32   afield4 #82
================================================================================
MSG: roslib/Header
#Standard metadata for higher-level flow data types
#sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""

	order = 2

	migrated_types = [
		("Header","Header"),
	]

	valid = True

	def update(self, old_msg, new_msg):
		self.migrate(old_msg.header, new_msg.header)
		new_msg.afield2 = old_msg.afield2
		new_msg.combo_field3 = old_msg.afield3 + ' ' + str(old_msg.afield1)
		new_msg.afield4 = old_msg.afield4

