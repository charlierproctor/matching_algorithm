# Stable Marriage Algorithm
# inspired by http://rosettacode.org/wiki/Stable_marriage_problem#Ruby

prefs = {
  'abe'  => %w[abi eve cath ivy jan dee fay bea hope gay],
  'bob'  => %w[cath hope abi dee eve fay bea jan ivy gay],
  'col'  => %w[hope eve abi dee bea fay ivy gay cath jan],
  'dan'  => %w[ivy fay dee gay hope eve jan bea cath abi],
  'ed'   => %w[jan dee bea cath fay eve abi ivy hope gay],
  'fred' => %w[bea abi dee gay eve ivy cath jan hope fay],
  'gav'  => %w[gay eve ivy bea cath abi dee hope jan fay],
  'hal'  => %w[abi eve hope fay ivy cath jan bea gay dee],
  'ian'  => %w[hope cath dee gay bea abi fay ivy jan eve],
  'jon'  => %w[abi fay jan gay eve bea dee cath ivy hope],
  'abi'  => %w[bob fred jon gav ian abe dan ed col hal],
  'bea'  => %w[bob abe col fred gav dan ian ed jon hal],
  'cath' => %w[fred bob ed gav hal col ian abe dan jon],
  'dee'  => %w[fred jon col abe ian hal gav dan bob ed],
  'eve'  => %w[jon hal fred dan abe gav col ed ian bob],
  'fay'  => %w[bob abe ed ian jon dan fred gav col hal],
  'gay'  => %w[jon gav hal fred bob abe col ed dan ian],
  'hope' => %w[gav jon bob abe ian dan hal ed col fred],
  'ivy'  => %w[ian col hal gav fred bob abe ed jon dan],
  'jan'  => %w[ed hal gav abe bob jon col ian fred dan],
}

class Person
  def initialize(name)
    @name = name
    @fiance = nil			# person object
    @preferences = []		# array of preferences -- person at 0 = top choice
    @proposals = []
  end

  attr_reader :name, :proposals
  attr_accessor :fiance, :preferences

  def to_s
    @name
  end

  def free
    @fiance = nil
  end

  def single?
    @fiance == nil
  end

  def engage(person)
    @fiance = person
    person.fiance = self
  end

  def better_choice?(person)
    @preferences.index(person) < @preferences.index(@fiance)
  end

  def propose_to(person)
    @proposals << person
    person.proposal_from(self)
  end

  def proposal_from(person)
    if single?
      engage(person)
    elsif better_choice?(person)
      @fiance.free
      engage(person)
    end
  end
end


@men = Hash[
  %w[abe bob col dan ed fred gav hal ian jon].collect do |name|
    [name,Person.new(name)]
  end
]

@women = Hash[
  %w[abi bea cath dee eve fay gay hope ivy jan].collect do |name|
    [name,Person.new(name)]
  end
]

@men.each do |name, man|
  man.preferences = @women.values_at(*prefs[name])
end
@women.each do |name, woman|
  woman.preferences = @men.values_at(*prefs[name])
end

def match(men,women)
  men.each_value {|man| man.free}
  women.each_value {|woman| woman.free}

  while m = men.values.find {|man| man.single?} do
      w = m.preferences.find {|woman| not m.proposals.include?(woman)}
      m.propose_to(w)
  end

end

  match(@men, @women)

  @men.each_value.collect {|man| puts "#{man} + #{man.fiance}"}

  # preference list contains DIFFERENT objects than primary men / women list
