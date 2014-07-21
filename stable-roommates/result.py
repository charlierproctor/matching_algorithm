import pprint

class Result:
	def __init__(self,ppl,unmatched,stable):
		self.ppl = ppl
		self.unmatched = unmatched
		self.stable = stable

	def print_nicely(self):
		if len(self.unmatched) > 0:
			#some people weren't matched
			print("The following individuals were unmatched:")
			for unmatched in self.unmatched:
				print(unmatched.name)
		else:
			#everybody was successfully matched
			print("Everybody is matched.\n")
			if self.stable:
				print("The match is stable.\n")
			else:
				print("The match is NOT stable.")
