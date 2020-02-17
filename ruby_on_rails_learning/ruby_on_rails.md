## Blocks
### Chunks of code
enclosed between either curly braces ({ }) or the keywords **do** and **end**
passed to methods as last "parameter"

### convention 
- use {} when block content is a single line
- use **do** & **end** when block content spans multiple lines
- often used as iterators

### Coding with blocks
#### Two ways to configure a block in your own method
1. implicit 
- use block_given? to see if block was passed in
- use yield to "call" the block
2. explicit
- use & in front of the last "parameter"
- use call method to call the block

### Summary
- Blocks are just code that you can pass into methods
- When incorporating into your own methods
- - *either* use blocks *implicitly*
- - *Or* call them *explicitly*

## Files
### Reading File
```
File.foreach('test.txt') do |line|
	put line
	p line
	p line.chomp # chops off newline character
	p line.split # array of words in line
	end
```

### Handling Exceptions
#### method1
```
begin
	File.foreach('do_not_exist.txt')do |line|
	puts line.chomp
	end

rescue Exception => e
	puts e.message
	puts "Let's pretend this didn't happen"
	end
```
#### method2 -simpler 
```
if File.exist? 'test.txt'
	File.foreach('test.txt') do|line|
		puts line.chomp
	end
end
```
### Writing to File
**The file is automatically closed after the block executes**
```
File.open("test1.txt","w") do|file|
	file.puts "One line"
	file.puts "Another"
end
```
### Environment Variables
`puts ENV["EDITOR"] #=> subl`


# Strings
- Single-quote literal strings are *very* literal
 - Allow escaping of \` with \
 - Show (almost) everything else *as is
- Double-quote strings
 - Interpret special characters like *\n* and *\t*
 - Allow string interpolation

## More Strings
1. String methods ending with ! modify the existing string
- most others just return a new string
2. Can also use %Q{long multiline string}
- Same behavior as double-quoted string

## VERY IMPORTANT SPRING API
go to ruby-doc.com/core-2.  /String.html

# Symbols
- :foo- highly optimized strings
- **Constant names** that you don't have to predeclare
- **"Stands for something"** string type

## Symbols 
- guaranteed to be *unique* & *immutable*
- can be converted to a *String* with to_s (vice is to_sym)

# Array
- Collection of object references(auto-expandable)
- indexed using [] operator(method)
- can be indexed with *negative numbers* or *ranges*
- Heterogeneous types allowed in the same way
- Can use %w{str1 str2} for string array creation

## Modifying arrays
- append: **push** or **<<**
- remove: pop or shift
- set: []= (method)
- randomly pull elements out with **sample**
- sort or reverse with sort! and reverse!
- *everything is a array*
- other
- each - loop through array
- select - filter array by selecting
- reject - filter array by rejecting
- map - modify each element in the array

# Ranges
used to express natural consecutive sequences
- 1..20, 'a'..'z'
- **TWO dots** -> all inclusive
- 1..10（1 is included, 10 is included)
- **Three dots** -> end-exclusive
- 1...10(1 is included, 10 is EXCLUDED)
- *waytoremember - the more dots you have, the less you have at the end*
- can be converted to an array with to_a
- used for conditions and intervals

# Hashes
- Indexed collections of object references
- Created with either {} or Hash.new
- Also known as *associative arrays*
- Index(key) can be anythign
 - **not just a integer** as in the case of arrays
- Accessed using the [] operator
- values set using => (creation) []  (post creation)
- *when access a valute which an entry does not exist* **nil is returned**
- *If Hash is created with Hash.new(0) 0 is returned instead*
- Hashes API is also important https://ruby-doc.org/core-2.2.0/Hash.html
- If a *hash* is the last argument to a method {} are optional
- Way1. adjust_colors ({:foreground =>green})
- Way2. adjust_colors background:"yella"
- Way3. adjust_colors :bakckground => "magenta"

## Block and Hash Confusion
\# Let's say you have a Hash
a_hash = {:one => "one"}

\# Then, you output it
puts a_has # => {:one => "one"}

but puts {:one => "one"} get a syntaxerror

\# ruby gets confused and thinks {} is a BLOCK!!

\# To get around this 
puts({:one => "one"}) 

\# Or drop the {} altogether..
puts one:"one"

# Classes

## Instance Variables
- Begin with @  @name
- not declared
 - spring into existence when first used
- available to all instance methods of the class
``` 
class Person
	def initialize(name, age) #"CONSTRUCTOR"
	@name = name
	@age = age
	end
	def get_info
		@additional_info = "Interesting"
		"Name: #{@name}, age: #{@age}"
	end
end

Person1 = Person.new("Joe", 14)
p Person1.instance_variables # [:@name, :@age]
puts Person1.get_info 
p Person1.instance_variables # [:@name, :@age, :@additional_info]
```

Accessing Data
- Instance variables are private
 - cannot be accessed from outside the class
- Methods have public access by default
- To access instance variables - need to define "getter" & "setter" methods
```
#in ruby getter&setter methods like this
def name
	@name
end
def name= (new_name)
	@name = new_name
end
```
//getter & setter简化的方法
attr_accessor - getter and setter
attr_reader -getter only
attr_writer - setter only

Solution: use a constructor & a more intellligent age setter

## self
- Inside instance method, self refers to the object itself
- Usually, using self for *calling other methods of the same instance is extraneous*
- outside instance method definition, self refers to the class itself
```
class Person
	attr_reader :age
	attr_accessor:name

	def initialize(name, ageVar)
	 @name = name
	 self.age = ageVar
	 puts age
	end
	def age= (new_age)
	 @age = new_age unless new_age > 120
	end
end
```
- don't forget self when required

# class inheritance
## || operator
|| operator evaluate left side
- If true - returns it
- Else - returns the right side
- @x = @x || 5 will return 5 the first time and @x the next time
- short for @x ||= 5

## Class methods and Variables
- **Invoked** on the **class** (as opposed to instance of class) like static method
- self **OUTSIDE** of the method definition refers to the Class object
- 3 ways to define class method in Ruby
- Class variables **begin** with @@
```
class MathFunctions
	def self.double(var)
		times_called
		var*2
	end
	class << self 
		def times_called
		@@times_called ||= 0
		@@times_called += 1
		end
	end
end
def MathFunctions.triple(var)
	times_called
	var*3
end
```

## class Inheritance
- every class implicitly inherits from Object
- Object itself inherits from BasicObject
- NO multiple inheritance
- Mixins are used instead
```
class Dog
	def to_s
	"Dog"
	end
	def bark
		"barks loudly"
	end
end
class SmallDog < Dog
	def bark #Overide
	 "barks quietly"
	end
end
```

# Modules
- **container** for classes, methods and constants
- like a Class, 但是不可以实例化
- class inherits from Module & adds new 
- 1. Namespace
- 2. mixin
Interfaces in OO
- Contract - define what a class "could" do
- Mixins provide a way to share (mix-in)ready code among multiple classes(**like Enumerable**)
```
class Player
	attr_reader: name, :age, :skill_level
	def initialize(name, age, skill_level)
		@name = name
		@age = age
		@skill_level = skill_level
	end

	def to_s
	 "<#{name}: #{skill_level}(SL), #{age}(AGE)>"
	end
end
```
- Team
```
class Team
	include Enumerable #LOTS of functionality
	attr_accessor :name, :players
	def initialize(name)
		@name = name
		@players = []
	end
	def add_players (*players)
		@players += players
	end
	def to_s
		"#{@name} team: #{@players.join(",")"
	end
	def each
		@player.each{|player|yield player}
	end
end
```
- 使用emuerable需要使用each方法
- require_relative is useful for *including other ruby files* relative to the *current ruby code*

# Scope
- Methods and classes begin new scope for variables
- 外部的变量不会到内部
- local_variables查看当前的变量
- constant常数，可以使用外部变量，这里和variable不同。内部定义的会覆盖外部的，出了，外部constant值不会改变

## Blocks
- block is a closure
- remembers the context in which it was defined and uses that context whenever it is called
- a variable created inside the block is only available to the block
- parameters to the block are always local to the block
- can explicitly declare block-local variables after a semicolon in the block parameter list

## Access Control
- methods in Ruby are public by default
```
class MyAlgorithm
	private
		def test1
			"Private"
		end
	protected
		def test2
			"Protected"
		end
	public
		def public_again
			"Public"
		end
end
```
```
class Another
	def test1
		"Private, as declared later on"
	end
	private :test1
end
```
- special - private methods - cannot be invoked with an explicit receiver
- 基本上只有构造函数，包括self.my_age这也是不允许的，但是self.age = age这个是允许的

# Introduction to Unit Testing
- ruby is a dynamic language
- unit test - serves as documentation for developers
- **Basic idea** - extended Test:: Unit:: TestCase
- Prefix method names with test_
- If one of the methods **fails** - others keep going
- can use setup() & teardown methods for setting up behavior that will execute before **every** test method
```
class CalculatorTest < Test::Unit::TestCase
	def setup
		@calc = Calculator.new('test')
	end

	def test_addition
		assert_equal 4, @calc.add(2,2)
	end

	def test_substraction
		assert_equal 2, @calc.subtract(4,2)
	end

	def test_division
		assert_equal 2, @calc,divide(4,2)
	end
end
```
- specifies the exception you expect and, in the coding block, when you expect it the exception to occur
- `assert_raise ZeroDivisionError do`

## RSpect
安装 gem install rspec
rspect --init
- describe(); before(); after(); setup(); teardown(); it()- take an optional string that **describe the behavior**
- related tests
```
require `rspec`
require_relative `../calculator`

describe Calculator do
	before { @calculator = Calculator.new('RSpec calculator')}

	it "should add 2 numbers correctly" do
		expect(@calculator.add(2,2)).to eq 4
	end
	
	it "should subtract 2 numbers correctly" do
		expect(@calculator.subtract(4,2)).to eq 2
	end
end
```
## Rspec Matchers
1. be_true/ be_false
2. eq 3
3. raise_error(SomeError)
- rspec --format documentation
- more https://relishapp.com/rspec

assignment1
The overall goal of this assignment is to implement a program control mechanism using Ruby that

properly tests for object equality
properly tests for a nil value
properly tests for a boolean true/false value
implements these tests using a case statement
The functional goal of the assignment is to rewrite a provided if/else statement using a case statement.

Please access the full description of the assignment and bootstrap files on github:

Instructions: https://github.com/jhu-ep-coursera/fullstack-course1-module2/blob/master/Assignments/Lesson01-Assignment01-Case-Statement/README.pdf
Bootstrap files: https://github.com/jhu-ep-coursera/fullstack-course1-module2/tree/master/Assignments/Lesson01-Assignment01-Case-Statement

assignment2
The overall goal of this assignment is to manipulate collections to derive a result.

The functional goal of the assignment is to chain a series of functions together to locate selected values within a collection.

Please access the full description of the assignment and bootstrap files on github:

instructions: https://github.com/jhu-ep-coursera/fullstack-course1-module2/blob/master/Assignments/Lesson02-Assignment01-Collections/README.pdf
Bootstrap files: https://github.com/jhu-ep-coursera/fullstack-course1-module2/tree/master/Assignments/Lesson02-Assignment01-Collections

assignment3
The overall goal of this assignment is to implement a Ruby class with

class attribute(s)
class method(s)
initializer method(s)
instance attribute(s)
instance method(s)
The functional goal of the assignment is to write a Person class that will maintain state thru instance and class attributes and provide access thru instance and class methods.

Please access the full description of the assignment and bootstrap files on github:

Instructions: https://github.com/jhu-ep-coursera/fullstack-course1-module2/blob/master/Assignments/Lesson03-Assignment01-Classes/README.pdf
Bootstrap files: https://github.com/jhu-ep-coursera/fullstack-course1-module2/tree/master/Assignments/Lesson03-Assignment01-Classes

