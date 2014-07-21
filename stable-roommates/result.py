from stats import GroupStat

class Result:
	def __init__(self,ppl,unmatched,stable):
		self.ppl = ppl
		self.unmatched = unmatched
		self.stable = stable

	def statify(self,group_stat):
		group_stat.increase_test_count()

		if len(self.unmatched) > 1:
			group_stat.increase_multiple_unmatched()
		elif len(self.unmatched) == 1:
			group_stat.increase_one_unmatched()

		if self.stable:
			group_stat.increase_stable_count()

	def print_nicely(self,group_size = 0):
		if group_size != 0:
			print("*"*80)
			print("Testing on Group Size: " + str(group_size) + "\n")
		if len(self.unmatched) > 0:
			#some people weren't matched
			print("The following individuals were unmatched:")
			for unmatched in self.unmatched:
				print(unmatched.name)
			print()
		else:
			#everybody was successfully matched
			print("Everybody is matched.\n")
			if self.stable:
				print("The match is stable.\n")
			else:
				print("The match is NOT stable.\n")
