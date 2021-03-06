class update_test_rosbagmigration_Convergent_fadc2231052dc3e2ecb5a84eea7e1e2d(MessageUpdateRule):
	old_type = "test_rosbagmigration/Convergent"
	old_full_text = """
float32   field1_a # 1.2
float32   field1_b # 3.4
float32   field1_c # 5.6
float32   field1_d # 7.8

SimpleMigrated     field2_a # 11
SimpleMigrated     field2_b # 22
SimpleMigrated     field2_c # 33
SimpleMigrated     field2_d # 44
================================================================================
MSG: test_rosbagmigration/SimpleMigrated
int32 data2 # 42
"""

	new_type = "test_rosbagmigration/Converged"
	new_full_text = """
float32[]   field1 # [1.2, 3.4, 5.6, 7.8]
SimpleMigrated[]    field2 # [11, 22, 33, 44]
================================================================================
MSG: test_rosbagmigration/SimpleMigrated
int32 data2 # 42
"""

	order = 0
	migrated_types = [('SimpleMigrated', 'SimpleMigrated')]

	valid = True

	def update(self, old_msg, new_msg):
		new_msg.field1 = [old_msg.field1_a, old_msg.field1_b, old_msg.field1_c, old_msg.field1_d]
                old_array = [old_msg.field2_a, old_msg.field2_b, old_msg.field2_c, old_msg.field2_d]
                self.migrate_array(old_array, new_msg.field2, 'SimpleMigrated')

class update_test_rosbagmigration_Converged_a47f409894343606276bb95cd2fd6b12(MessageUpdateRule):
	old_type = "test_rosbagmigration/Converged"
	old_full_text = """
float32[]   field1 # [1.2, 3.4, 5.6, 7.8]
SimpleMigrated[]    field2 # [11, 22, 33, 44]
================================================================================
MSG: test_rosbagmigration/SimpleMigrated
int32 data2 # 42
"""

	new_type = "test_rosbagmigration/Converged"
	new_full_text = """
float32[4]           field1 # [1.2, 3.4, 5.6, 7.8]
SimpleMigrated[4]    field2 # [11, 22, 33, 44]
================================================================================
MSG: test_rosbagmigration/SimpleMigrated
int32 data3 # 42
"""

	order = 0
	migrated_types = [('SimpleMigrated', 'SimpleMigrated')]

	valid = True

	def update(self, old_msg, new_msg):
		new_msg.field1 = old_msg.field1
		self.migrate_array(old_msg.field2, new_msg.field2, 'SimpleMigrated')

