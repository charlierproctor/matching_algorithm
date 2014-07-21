# Stable Roommate Algorithm
import pprint, sys
from tester import Tester 

# adjust the system's recursion call depth limit
# default of 1000
sys.setrecursionlimit(10000)

# standard stable roommate preference array (from wikipedia)
# prefs = Tester.wiki_roommate

# standard stable marriage preference array (from rosetta code)
# prefs = Tester.rosetta_marriage

# random preference array generator in tester.py
prefs = Tester.random_matrix(12)


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
	def prefsMatrix(time):
		res = {}
		for person_name,person_object in Person.ppl.items():
			res[person_name] = person_object.getPrefs(time)
		return res

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
	def were_people_matched():
		ppl_without_match = []
		for person_name,person_object in Person.ppl.items():
			if len(person_object.current_prefs) != 1:
				# they don't have a match!
				ppl_without_match.append(person_object)
		if len(ppl_without_match) > 0:
			#some people weren't matched
			print("The following individuals were unmatched:")
			for unmatched in ppl_without_match:
				print(unmatched.name)
		else:
			#everybody was successfully matched
			print("Everybody was matched.\n")


# SETUP --> CREATE PERSON OBJECTS

Person.setup(prefs)

print("Starting Preference Matrix -- Phase 0 Complete:")
pprint.pprint(Person.prefsMatrix('current'))

# PHASE 1

#core of phase 1 --> everybody proposes to their top choice
for person in Person.ppl.values():
	# before proposing, we need to make sure everybody hasn't rejected them yet!
	# this would happen iff everybody else has already received better offers...
	if len(person.current_prefs) > 0:       
		person.propose_to(person.current_prefs[0])  # propose to your top choice

print("Phase 1 Complete:")
pprint.pprint(Person.prefsMatrix('current'))


# PHASE 2

#find the initial person with a second column
current_person = Person.find_person_with_second_column()    

num_rotations = 1    # number of rotations so far...

# while we still have a person with a second column
while current_person: 

	# grab their second choice preference
	current_pref = current_person.current_prefs[1]

	# and cross off that person's last preference.... 
	# which kicks off the rotation
	current_pref.cross_off(current_pref.current_prefs[-1])

	print("Rotating around person " + current_person.name + 
		", with preference " + current_pref.name)
	print("Rotation #" + str(num_rotations) + ":")

	num_rotations = num_rotations + 1
	pprint.pprint(Person.prefsMatrix('current'))	

	# find another person to work with... if there is one
	current_person = Person.find_person_with_second_column()


print("Phase 2 Complete:")
pprint.pprint(Person.prefsMatrix('current'))

print("\nRESULTS:\n")

Person.were_people_matched()




