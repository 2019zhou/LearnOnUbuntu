class Person
  #have a first_name and last_name attribute with public accessors
  attr_accessor :first_name, :last_name

  #have a class attribute called `people` that holds an array of objects
  @@people = []

  #have an `initialize` method to initialize each instance
  def initialize(x,y)#should take 2 parameters for first_name and last_name
    #assign those parameters to instance variables
    @first_name = x
    @last_name = y
    #add the created instance (self) to people class variable
    @@people.push(self)
  end


  #have a `search` method to locate all people with a matching `last_name`
  def self.search(last_name)
    #accept a `last_name` parameter
    _collection = []
    @@people.each do |name|
       _collection.push name.to_s if name.last_name == last_name
    end
    #search the `people` class attribute for instances with the same `last_name`
    _collection
    #return a collection of matching instances
  end
  #have a `to_s` method to return a formatted string of the person's name

  def to_s
    #return a formatted string as `first_name(space)last_name`
     "#@first_name #@last_name"
  end
end

p1 = Person.new("John", "Smith")
p2 = Person.new("John", "Doe")
p3 = Person.new("Jane", "Smith")
p4 = Person.new("Cool", "Dude")

puts Person.search("Smith")

=begin
p.each do |name|
  puts name.to_s
end
=end

# Should print out
# => John Smith
# => Jane Smith
