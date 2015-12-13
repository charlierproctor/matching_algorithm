# a person class - this defines most of the key matching methods

class Person:
	def __init__(self, name):
		self.name = name
		self.initial_prefs = []   # a person's initial set of preferences
		self.current_prefs = []     # a person's current set of preferences

	# class variable to store all the people
	ppl = {}

	#somebody is going to propose!!
	def propose_to(self,somebody):
		somebody.receive_proposal_from(self)

	# when somebody receives a proposal in phase 1
	def receive_proposal_from(self,somebody):
		current_prefs = self.current_prefs

		# need to cross off those behind current proposal
		prefs_to_chop = current_prefs[(current_prefs.index(somebody)+1):]  
		# this is what causes a rotation to halt!! 
			# --> ie, we have reached another stable table
		# when there is nobody left to cross off.

		#use the cross_off method to cross off these matches...
		for person in prefs_to_chop:
			self.cross_off(person)

	# crosses off a potential match
	def cross_off(self,person):
		#removes each from each other's preference array
		if person in self.current_prefs:       
			self.current_prefs.remove(person)
		if self in person.current_prefs:
			person.current_prefs.remove(self)

		#initiate a new proposal
		if len(person.current_prefs) > 0:
			person.propose_to(person.current_prefs[0])     
		# why do they always propose to their top choice??  
		# (even if we haven't crossed off their old top choice?)
	
	# find a person who still has a second column
	# return False if there is no person left
	@staticmethod
	def find_person_with_second_column():
		res = False
		for person in Person.ppl.values():
			if len(person.current_prefs) > 1:
				res = person
				break
		return res

	#return just the names of the people in the preference arrays
	def getPrefs(self,time):
		res = []
		if time == 'initial':
			for pref in self.initial_prefs:
				res.append(pref.name)
		else:
			for pref in self.current_prefs:
				res.append(pref.name)
		return res

	# generates the hash to display all people's preferences
	@staticmethod
	def prefsMatrix(time):
		res = {}
		for person_name,person_object in Person.ppl.items():
			res[person_name] = person_object.getPrefs(time)
		return res

	@staticmethod
	def setup(prefs):
		# create ppl hash which have names as keys
		# and the corresponding person objects as values
		for person in prefs:
			Person.ppl[person] = Person(person)

		# add the appropriate person objects to their preference array
		for person_name,person_object in Person.ppl.items():   # the person
			for pref_name in prefs[person_name]:      #their current_prefs
				# populate the initial preference array
				person_object.initial_prefs.append(Person.ppl[pref_name])
				# populate the current preference array
				person_object.current_prefs.append(Person.ppl[pref_name])

	# determines whether everybody was matched
	@staticmethod
	def who_wasnt_matched():
		ppl_without_match = []
		for person_name,person_object in Person.ppl.items():
			if len(person_object.current_prefs) != 1:
				# they don't have a match!
				ppl_without_match.append(person_object)
		return ppl_without_match

	def better_prefs(self):
		initial_prefs = self.initial_prefs
		# pprint.pprint(initial_prefs)
		final_prefs = self.current_prefs
		match = final_prefs[0]
		better_prefs = initial_prefs[:initial_prefs.index(match)]
		def person_name_string(obj):
			return obj.name
		# print(self.name + "," + str(list(map(person_name_string,better_prefs))))
		return better_prefs

	@staticmethod
	def was_the_match_stable():
		stable = True
		for my_name, my_object in Person.ppl.items():
			my_better_ppl = my_object.better_prefs()
			for person in my_better_ppl:
				their_better_ppl = person.better_prefs()
				if my_object in their_better_ppl:
					stable = False
					break
		return stable

	@staticmethod
	def empty_column():
		empty = False
		for person in Person.ppl.values():
			if len(person.current_prefs) == 0:
				empty = True
				break
		return empty
