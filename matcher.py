guyprefers = {
 'abe':  ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
 'bob':  ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
 'col':  ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
 'dan':  ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
 'ed':   ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
 'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
 'gav':  ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
 'hal':  ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
 'ian':  ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
 'jon':  ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']}
galprefers = {
 'abi':  ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
 'bea':  ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
 'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
 'dee':  ['fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
 'eve':  ['jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
 'fay':  ['bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
 'gay':  ['jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
 'hope': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
 'ivy':  ['ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
 'jan':  ['ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']}
 
class Person:
	def __init__(self, name):
		self.name = name
		self.fiance = None
		self.preferences = []
		self.proposals = []

	def __str__(self):
		return self.name

	def free(self):
		self.fiance = None

	def single(self):
		return self.fiance == None

	#engage somebody
	def engage(self, person):
		self.fiance = person
		person.fiance = self

	#determine whether the person is a better choice (higher in the list)
	def better_choice(self, person):
		print(self.name + " is evaluating her options...")
		if self.preferences.index(person) < self.preferences.index(self.fiance):
			print(self.name + " decides " + person.name + " is a better choice than current fiance " + self.fiance.name)
		else:
			print(self.name + " decides " + person.name + " is a worse choice than current fiance " + self.fiance.name)
		# print(self.preferences.index(person) < self.preferences.index(self.fiance))
		return self.preferences.index(person) < self.preferences.index(self.fiance)
  
  	#propose to somebody
	def propose_to(self,person):
		self.proposals.append(person)
		person.proposal_from(self)

	#receive a proposal from the opposite sex
	def proposal_from(self, person):
		#if single, accept!
		if self.single():
			self.engage(person)
			print(self.name + " is single and accepts " + person.name + "'s proposal")
		#if the proposer is a better choice, accept!
		elif self.better_choice(person):
			print(self.name + " is dumping " + self.fiance.name + " for " + person.name)
			self.fiance.free()
			self.engage(person)
		#otherwise, reject!
		else:
			print(self.name + " rejects " + person.name + " to keep " + self.fiance.name)


# create men, women hashes which have names as keys
# and the corresponding person objects as values
men = {}
for guy in guyprefers:
	men[guy] = Person(guy)

women = {}
for gal in galprefers:
	women[gal] = Person(gal)

# for all men, add the appropriate women objects to
# their preference arrays
for man_name,man_object in men.items():
	for woman_name in guyprefers[man_name]:
		man_object.preferences.append(women[woman_name])

# for all women...
for woman_name,woman_object in women.items():
	for man_name in galprefers[woman_name]:
		woman_object.preferences.append(men[man_name])

#find all the single men
def find_single(gender):
	print("Looking for single men...")
	for person,person_object in gender.items():
		if person_object.single():
			print(person_object.name + " is single")
			return person_object
	print("Nobody is single...")
	return False

#find the man's next top choice (whom he has yet to propose to)
def find_next_best(man,women):
	for woman in man.preferences:
		if not (woman in man.proposals):
			print(man.name + "'s next choice is " + woman.name)
			return woman

#method to free everybody of their spouse
def free_everybody():
	for man in men:
		men[man].free()
	for woman in women:
		women[woman].free()

#core matching method
def match(men,women):
	free_everybody()

	done = False

	while not done:
		#find the single men
		man = find_single(men)
		if not man:
			#if there aren't any, we're done
			done = True
		else:
			#if there are, find the next best woman, and propose to her
			woman = find_next_best(man,women)
			print(man.name + " is proposing to " + woman.name)
			man.propose_to(woman)

#perform the match
match(men,women)

#print the results
print("\nTHE RESULTS\n")
for man_name,man_object in men.items():
	print(man_name + ", " + man_object.fiance.name)


