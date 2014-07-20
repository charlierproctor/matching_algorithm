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
prefs = Tester.random_matrix(100)


class Person:
	def __init__(self, name):
		self.name = name
		self.preferences = []

	# class variable to store all the people!
	ppl = {}

	#somebody is going to propose!!
	def propose_to(self,somebody):
		somebody.receive_proposal_from(self)

	# when somebody receives a proposal in phase 1
	def receive_proposal_from(self,somebody):
		current_prefs = self.preferences

		# need to cross off those behind current proposal
		prefs_to_chop = current_prefs[(current_prefs.index(somebody)+1):]  
		# this is what causes a rotation to halt!! --> ie, we have reached another stable table
		# when there is nobody left to cross off.

		#use the cross_off method to cross off these matches...
		for person in prefs_to_chop:
			self.cross_off(person)

	# crosses off a potential match
	def cross_off(self,person):
		#removes each from each other's preference array
		if person in self.preferences:       
			self.preferences.remove(person)
		if self in person.preferences:
			person.preferences.remove(self)

		#initiate a new proposal
		if len(person.preferences) > 0:
			person.propose_to(person.preferences[0])

	#return just the names of the people in the preferences
	def getPrefs(self):
		res = []
		for pref in self.preferences:
			res.append(pref.name)
		return res

	# generates the hash to display all people's current preferences
	def prefsMatrix():
		res = {}
		for person_name,person_object in Person.ppl.items():
			res[person_name] = person_object.getPrefs()
		return res

# SETUP --> CREATE PERSON OBJECTS

# create ppl hash which have names as keys
# and the corresponding person objects as values
for person in prefs:
	Person.ppl[person] = Person(person)

# add the appropriate person objects to their preference array
for person_name,person_object in Person.ppl.items():   # the person
	for pref_name in prefs[person_name]:      #their preferences
		person_object.preferences.append(Person.ppl[pref_name])

print("Starting Preference Matrix -- Phase 0 Complete:")
pprint.pprint(Person.prefsMatrix())

# PHASE 1

# whether phase one was successful...
# ie, the first columns hold distinct people
def phase_one_success():
	arr = []
	for person in Person.ppl.values():  
		arr.append(person.preferences[0].name)
	return len(arr)==len(set(arr))

#core of phase 1 --> everybody proposes to their top choice
for person in Person.ppl.values():
	person.propose_to(person.preferences[0])

if not phase_one_success():
	print("PHASE 1 FAILURE -- NO STABLE MATCHING POSSIBLE")

print("Phase 1 Complete:")
pprint.pprint(Person.prefsMatrix())


# PHASE 2

# find a person who still has a second column
# return False if there is no person left
def find_person_with_second_column():
	res = False
	for person in Person.ppl.values():
		if len(person.preferences) > 1:
			res = person
			break
	return res

current_person = find_person_with_second_column()    #find the initial person with a second column

num_rotations = 1    # number of rotations so far...

# while we still have a person with a second column
while current_person: 

	# grab their second choice preference
	current_pref = current_person.preferences[1]

	# and cross off that person's last preference.... which kicks off the rotation
	current_pref.cross_off(current_pref.preferences[-1])

	print("Rotating around person " + current_person.name + ", with preference " + current_pref.name)
	print("Rotation #" + str(num_rotations) + ":")

	num_rotations = num_rotations + 1
	pprint.pprint(Person.prefsMatrix())	

	# find another person to work with... if there is one
	current_person = find_person_with_second_column()


print("Phase 2 Complete:")
pprint.pprint(Person.prefsMatrix())


