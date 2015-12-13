# a class to track stats related to testing the algorithm multiple times 
# on different group sizes

class GroupStat:
	# each object is for a different group size

	# class variables to track overall results
	total_one_unmatched = 0
	total_multiple_unmatched = 0
	total_stable_count = 0
	total_tests = 0
	all_groups = []

	def __init__(self,group_size):
		self.group_size = group_size
		GroupStat.all_groups.append(self)

		#instance variables to track results in this particular group size
		self.one_unmatched = 0
		self.multiple_unmatched = 0
		self.stable_count = 0
		self.test_count = 0

	# methods to increase various result counts...
	def increase_test_count(self):
		GroupStat.total_tests = GroupStat.total_tests + 1
		self.test_count = self.test_count + 1

	def increase_one_unmatched(self):
		self.one_unmatched = self.one_unmatched + 1
		GroupStat.total_one_unmatched = GroupStat.total_one_unmatched + 1

	def increase_multiple_unmatched(self):
		self.multiple_unmatched = self.multiple_unmatched + 1
		GroupStat.total_multiple_unmatched = GroupStat.total_multiple_unmatched + 1

	def increase_stable_count(self):
		self.stable_count = self.stable_count + 1
		GroupStat.total_stable_count = GroupStat.total_stable_count + 1

	# methods to calculate percentages
	@staticmethod
	def total_percent_stable():
		return round(GroupStat.total_stable_count / GroupStat.total_tests * 100,2)

	@staticmethod
	def total_percent_one_unmatch():
		return round(GroupStat.total_one_unmatched / GroupStat.total_tests * 100,2)		

	@staticmethod
	def total_percent_multiple_unmatched():
		return round(GroupStat.total_multiple_unmatched / GroupStat.total_tests * 100,2)

	# method to nicely display the results for a GroupStat
	@staticmethod
	def print_nicely():
		print("*"*80)			# a header of sorts...
		print("Size \t\t Tests \t\t One \t\t Mult. \t\t Stable")
		print("*"*80)

		# individual GroupStat results (results for each different group size)
		for group in GroupStat.all_groups:
			print(str(group.group_size) + "\t\t" + str(group.test_count) + "\t\t" +
				str(group.one_unmatched) + "\t\t" + str(group.multiple_unmatched)
				+ "\t\t" + str(group.stable_count))

		# overall results (as a sum of GroupStat results)
		print("*"*80)
		print("SUM" + "\t\t" + str(GroupStat.total_tests) + "\t\t" +
			str(GroupStat.total_one_unmatched) + "\t\t" 
			+ str(GroupStat.total_multiple_unmatched) 
			+ "\t\t" + str(GroupStat.total_stable_count))		
		print("*"*80)

		# overall results (percentages)
		print("Percent One Unmatch: " + str(GroupStat.total_percent_one_unmatch()))
		print("Percent Multiple Unmatch: " + str(GroupStat.total_percent_multiple_unmatched()))				
		print("*"*80)		
		print("Percent Stable: " + str(GroupStat.total_percent_stable()))
		print("*"*80)
