# PYTHON OOP

Summary of `OOP` in `Python`

## Review

The main concepts of `OOP` are:
1. `Class` - the `blueprint` or `collection` of `Objects`
2. `Objects` - an `entity` that has a `state` and `behaviour` and is `unique`
3. `Polymorphism` - having _many_ (`poly`) forms
4. `Inheritance` - a property where one `class` has the capability to _derive_ or _inherit_ the properties from another `class`
5. `Encapsulation` - a _fundamental_ concept where `data` and `methods` are contained within _one unit_ (e.g., a `class`)

### Class

In `python`, a `class` is created with the `keyword` `class`. Any `attributes` are the _variables_ that belong to a `class.
- Attributes are public
- They are accessed with a `dot (.)` operator

``` Python
# class is Ring and it has an attribute of size
Ring.size
```
We would setup or _define_ a class with the following `syntax`:

``` Python
class ClassName:
  # Statement -1
  .
  .
  .
  # Statement -N
```
Don't forget `pass` is useful when we aren't sure what we want to do yet (have a place holder to skip over) or if we want to create an empty `class`:

```Python
class Ring:
  pass
```
We must initialize with `__init__`:

```Python
class Ring(object):
  def __init__(self, size):
    self.size = size
```

### Objects

In general, `Objects` can be _any_ single interger or single string. An example could also be a `python` `list` which is an `Object` that can hold _other_ `objects`. 

`Objects` consist of:
1. `State`: reflects the _properties_ of an `Object` and is represented by the _attributes_ of an `Object`
2. `Behaviour`: reflects the _response_ of an `Object` to _other_ `Objects` and is represented by the _methods_ of an `Object`
3. `Identity`: provides the `Object` with a _unique_ name, enabling one `Object` to interact with other `Objects`

```Python
class Ring(object):
  def __init__(self, x, y):
    self.x = x # x-coordinate
    self.y = y # y-coordinate
```
So lets make an `object`:

```Python
ring1 = Ring(0, 0) # Create an object called ring1 of class Ring initialized with (x,y) values equal to (0,0)
```

### Polymorphism

Our `Objects`, as _instances_ of our `Class`, can have _many_ forms. For example: 

```Python
class Ring:
  def intro(self):
    print("There are many types of rings.")
  
  def shape(self):
    print("Most rings are round.")

class wedding(Ring):
  def shape(self):
    print("Wedding rings are round.")

class friendship(Ring):
  def shape(self):
    print("Friendship rings are not round.")

object1_ring = Ring()
object2_wedding = wedding()
object3_friend = friendship()

object1_ring.intro()
object1_ring.shape()

object2_wedding.intro()
object2_wedding.shape()

object3_friend.intro()
object3_friend.shape()
```
Our output:

```Terminal
There are many types of rings.
Most rings are round.
There are many types of rings.
Wedding rings are round.
There are many types of rings.
Friendship rings are not round.
```

### Inheritance

Notice how in our earlier example, since we did _not_ change the `parent` `Class` for _Ring.info_, our `children` retained this attribute. This is an example of `inheritance`.

```Python
class Ring:
  def intro(self):
    print("There are many types of rings.")
  
  def shape(self):
    print("Most rings are round.")

class wedding(Ring):
  def shape(self):
    print("Wedding rings are round.")

object1_ring = Ring()
object2_wedding = wedding()

object1_ring.intro()
object1_ring.shape()

object2_wedding.intro()
object2_wedding.shape()
```
Our output:

```Terminal
There are many types of rings.
Most rings are round.
There are many types of rings.
Wedding rings are round.
```

Our `Object` _object2_wedding_ has retained `Object` _object1_ring_'s .info property. It was `inherited`. So, in this example, our _derived class_ or _child class_ are _wedding_ wedding(Ring), and these rings are inheriting, or deriving their properties from our _base class_ or _parent class_ defined as Ring().

Some benefits of `inheritance`:
1. Easily represents real-world relationships
2. Easy to re-use code and add more features to class without _modifying_ the `Class`
3. Transitive - if wedding(Ring) inherits from Ring(), then my_ring(wedding) and your_ring(wedding) automatically `inherit` from `class` Ring() too!

```Python
class Ring:
  def intro(self):
    print("There are many types of rings.")
  
  def shape(self):
    print("Most rings are round.")

class wedding(Ring):
  def shape(self):
    print("Wedding rings are round.")

class mine(wedding):
  def shape(self):
    print("ouch a triangle.")

object1_ring = Ring()
object2_wedding = wedding()
object3_myRing = mine()

object1_ring.intro()
object1_ring.shape()

object2_wedding.intro()
object2_wedding.shape()

object3_myRing.intro()
object3_myRing.shape()
```

Our output:

```Terminal
There are many types of rings.
Most rings are round.
There are many types of rings.
Wedding rings are round.
There are many types of rings.
ouch a triangle.
```

### Encapsulation

**Note:** The concept is for all students; this example is for more advanced students.

By _wrapping_ our data and methods into one unit it is possible to _restrict_ variable and method access. We could set our `Class` up such that an `Object`'s variable could _only_ be changed by an `Object`'s method (making it a _private_ variable):

```Python
# Creating a Base class
class BaseParent():
  def __init__(self):
    self.name = "Hi it's me!"
    self.__privatename = "Hi it's me!"

# Creating a derived class
class DerivedChild(BaseParent):
  def __init__(self):
    # Calling constructor of Base class
    BaseParent.__init__(self)
    print("Calling private member of base class: ")
    print(self.__privatename)

object1 = BaseParent()
print(object1.name)

# Uncomment to demo an AttributeError
print(object1.othername)

# Uncomment to demo an another AttributeError
object2 = DerivedChild() 
```

Output (with the uncommented sections one by one):

``` Terminal
// uncommented print(object1.othername)
Traceback (most recent call last):
  File "test.py", line 19, in <module>
    print(object1.othername)
AttributeError: 'BaseParent' object has no attribute 'othername'

Hi it's me!
```
and the second AttributeError is:

``` Terminal
// uncommented object2 = DerivedChild()
Traceback (most recent call last):
  File "test.py", line 22, in <module>
    object2 = DerivedChild()
  File "test.py", line 13, in __init__
    print(self.__privatename)
AttributeError: 'DerivedChild' object has no attribute '_DerivedChild__privatename'

Hi it's me!
Calling private member of base class:
```

What happend? We created the _privatename_ `variable` as a _private_ `attribute`; we _can't directly access_ this `attribute` and we _can't change_ its `value`.

### NOTE ABOUT CONVENTION

`Protected members` (in `C++` and `JAVA`) are those members of the `class` that _cannot be accessed outside the `class`_ but _can be accessed from within the `class` and its `subclasses`. To accomplish this in `Python`:
- follow the convention by `prefixing` the name of the member by a single underscore `“_”`.

In `Python` however, `mangling` allows this convention to be broken (the `protected` variable _can_ be accessed out of the `class`)
- So? We follow the customs of `C++` and `JAVA` and do _not_ access the `protected` variable outside of the `class`
- this is not a `rule` but a `convention`

>
> Note: The `__init__` method is a _constructor_ and runs as soon as an object of a class is instantiated.  

---

## Other aspects

1. Subclassing - calling the _constructor_ of a `parent` `Class`: a `child` `Class` must _identify_ which `Class` is its _`parent`_
```Python
class subclass_name(superclass_name):
```
2. Python supports _multiple inheritance_ or `inheritance` from _multiple `parent` classes_: use a _comma-separated_ `list`
```Python
class Child(Parent1, Parent2):
```
3. Multi-_level_ `inheritance`: we start adding more _family members_ (like... `grandchildren` - I did it earlier)
```Python
class Ring(object): # Parent(object)

class wedding(Ring): # Child(Parent)

class myRing(wedding): # Grandchild(Child)
```

There are even more types of `inheritance`:

4. Hierarchical inheritance
5. Hybrid inheritance

... and we can define whether or not instances (`children`) inherit private variables (from `parent`)
