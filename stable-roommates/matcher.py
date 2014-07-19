# Stable Roommate Algorithm
import pprint
prefs = {
'1': ['3','4','2','6','5'],
'2': ['6','5','4','1','3'],
'3': ['2','4','5','1','6'],
'4': ['5','2','3','6','1'],
'5': ['3','1','2','4','6'],
'6': ['5','1','3','4','2']}


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

		#use the cross_off method to cross off these matches...
		for person in prefs_to_chop:
			self.cross_off(person)

	# crosses off a potential match
	def cross_off(self,person):
		#removes each from each other's preference array
		self.preferences.remove(person)
		person.preferences.remove(self)
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

def phase_one_success():
	arr = []
	for person in Person.ppl.values():  
		arr.append(person.preferences[0].name)
	return len(arr)==len(set(arr))

for person in Person.ppl.values():
	person.propose_to(person.preferences[0])

if not phase_one_success():
	print("PHASE 1 FAILURE -- NO STABLE MATCHING POSSIBLE")

print("Stable Table -- Phase 1 Complete:")
pprint.pprint(Person.prefsMatrix())


# PHASE 2

def find_person_with_second_column():
	res = False
	for person in Person.ppl.values():
		if len(person.preferences) > 1:
			res = person
			break
	return res

current_person = find_person_with_second_column()

num_rotations = 1

while current_person: 
	current_pref = current_person.preferences[1]
	current_pref.cross_off(current_pref.preferences[-1])

	print("Rotation #" + str(num_rotations) + ":")
	num_rotations = num_rotations + 1
	pprint.pprint(Person.prefsMatrix())	

	current_person = find_person_with_second_column()


print("Phase 2 Complete:")
pprint.pprint(Person.prefsMatrix())




