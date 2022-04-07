# SUPER time to read this!!

Summary of `Inheritance` `options` in `Python`

## Review

The main idea of this page is to review, remind about:

1. The concept of inheritance in Python
2. Multiple inheritance in Python
3. How the `super()` function works
4. How the `super()` function in single inheritance works
5. How the `super()` function in multiple inheritance works

### Python’s `super()` Function

`super()` gives you access to methods in a superclass from the subclass that inherits from it.

`super()` alone returns a temporary object of the superclass that then allows you to call that superclass’s methods.

Why would you want to do any of this? While the possibilities are limited by your imagination, a common use case is building classes that extend the functionality of previously built classes.

Calling the previously built methods with `super()` saves you from needing to rewrite those methods in your subclass, and allows you to swap out superclasses with minimal code changes.

## `super()` in Single Inheritance

`Inheritance` is a concept in `object-oriented programming` in which a `class` derives (or inherits) `attributes` and `behaviors` from another `class` _without needing to implement them again_.

Let’s write `classes` describing some `shapes`:

```Python
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

  def perimeter(self):
    return 2 * self.length + 2 * self.width

class Square:
  def __init__(self, length):
    self.length = length

  def area(self):
    return self.length * self.length

  def perimeter(self):
    return 4 * self.length
```

Here, there are two similar classes: `Rectangle` and `Square`.
Let's use them:

```Python
>>> square = Square(4)
>>> square.area()
16
>>> rectangle = Rectangle(2,4)
>>> rectangle.area()
8
```

In this example, you have two shapes that are related to each other: a square is a special kind of rectangle. The code, however, _doesn’t reflect that relationship and thus has code that is essentially repeated_.

By using `inheritance`, you can _reduce the amount of code you write_ while _simultaneously reflecting the real-world relationship_ between rectangles and squares:

```Python
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

  def perimeter(self):
    return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)
```

Here, you’ve used `super()` to call the `__init__()` of the `Rectangle` class, allowing you to use it in the `Square` class without repeating code. Below, the core functionality remains after making changes:

```Python
>>> square = Square(4)
>>> square.area()
16
```

In this example, `Rectangle` is the _superclass_, and `Square` is the _subclass_.

Because the `Square` and `Rectangle` `.__init__()` `methods` are so similar, you can simply call the superclass’s `.__init__()` method (`Rectangle.__init__()`) from that of `Square` by using `super()`. This sets the `.length` and `.width` `attributes` _even though you just had to supply a single length parameter_ to the `Square` `constructor`.

When you run this, even though your `Square` class doesn’t explicitly implement it, the call to `.area()` will use the `.area()` method in the superclass and print 16. `The Square` class _inherited_ `.area()` from the `Rectangle` class.

---

## what can `super()` do for you in single inheritance?

Like in other `object-oriented languages`, it allows you to call methods of the superclass in your subclass. The primary use case of this is to _extend the functionality of the inherited method_.

In the example below, you will create a class `Cube` that inherits from `Square` and _extends the functionality_ of `.area()` (_inherited_ from the `Rectangle` class _through_ `Square`) to calculate the surface area and volume of a `Cube` `instance`:

```Python
class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)

class Cube(Square):
  def surface_area(self):
    face_area = super().area()
    return face_area * 6

  def volume(self):
    face_area = super().area()
    return face_area * self.length
```

Now that you’ve built the classes, let’s look at the surface area and volume of a cube with a side length of 3:

``` Pyhton
>>> cube = Cube(3)
>>> cube.surface_area()
54
>>> cube.volume()
27
```
>
> Caution: Note that in our example above, `super()` alone won’t make the method calls for you: you have to call the method on the proxy object itself.
>

Here you have implemented two methods for the `Cube` class: `.surface_area()` and `.volume()`. Both of these calculations rely on calculating the area of a single face, so rather than reimplementing the area calculation, you use `super()` to _extend_ the area calculation.

Also notice that the `Cube` class definition does not have an `.__init__()`. Because `Cube` _inherits from `Square`_ and `.__init__()` doesn’t really do anything differently for `Cube` than it already does for `Square`, you can skip defining it, and the `.__init__()` of the _superclass_ (`Square`) will be called automatically.

`super()` returns a delegate object to a parent class, so you call the method you want directly on it: `super().area()`.

Not only does this save us from having to rewrite the area calculations, but it also allows us to change the internal `.area()` logic in a single location. This is especially in handy when you have a number of subclasses inheriting from one superclass.

---

### quick detour into the mechanics of super()

Let's take a quick look at the mechanics of `super()`.

While the examples above (and below) call `super()` _without any parameters_, `super()` can also take _two_ parameters: the first is _the subclass_, and the second parameter is an `object` that is an _instance of that subclass_.

First, let’s see two examples showing what manipulating the first variable can do, using the classes already shown:

```Python
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

  def perimeter(self):
    return 2 * self.length + 2 * self.width

class Square(Rectangle):
  def __init__(self, length):
    super(Square, self).__init__(length, length)
```

In Python 3, the `super(Square, self)` call is equivalent to the parameterless `super()` call. The first parameter refers to the `subclass` `Square`, while the second parameter refers to a `Square` `object` which, in this case, is _`self`_. You can call `super()` with other classes as well:

```Python
class Cube(Square):
  def surface_area(self):
    face_area = super(Square, self).area()
    return face_area * 6

  def volume(self):
    face_area = super(Square, self).area()
    return face_area * self.length
```

In this example, you are setting `Square` as the subclass argument to `super()`, _instead_ of `Cube`. This causes `super()` to start searching for a matching method (in this case, `.area()`) at _one level above_ `Square` in the _instance hierarchy_, in this case `Rectangle`.

In this specific example, the behavior doesn’t change. But imagine that `Square` also implemented an `.area()` function that you wanted to make sure `Cube` did _not_ use. Calling `super()` in this way allows you to do that.

>
> Caution: While we are doing a lot of fiddling with the parameters to `super()` in order to explore how it works under the hood, I’d caution against doing this regularly.
>
> The parameterless call to `super()` is recommended and sufficient for most use cases, and needing to change the search hierarchy regularly could be indicative of a larger design issue.
>

What about the second parameter? Remember, this is an object that is an instance of the class used as the first parameter. For an example, `isinstance(Cube, Square)` must return `True`.

By including an instantiated object, `super()` returns a bound method: a method that is bound to the object, which gives the method the object’s context such as any instance attributes. If this parameter is not included, the method returned is just a function, unassociated with an object’s context.

>
> Note: Technically, `super()` doesn’t return a method. It returns a proxy object. This is an object that delegates calls to the correct class methods without making an additional object in order to do so.
>

---

## super() in Multiple Inheritance

Now that you’ve worked through an overview and some examples of `super()` and single inheritance, you will be introduced to an overview and some examples that will demonstrate
how multiple inheritance works and how `super()` enables that functionality.

There is another use case in which `super()` really shines, and this one isn’t as common as the single inheritance scenario. In addition to single inheritance, `Python` supports multiple inheritance, in which a subclass can inherit from multiple superclasses that don’t necessarily inherit from each other (_also known as sibling classes_).

Here's a diagram from the course source, could be helpful to understand concepts like this. The image below shows a very simple multiple inheritance scenario, where one class inherits from two unrelated (sibling) superclasses:

![image](/Code/references/super.png) "Subclass inherits from two sibling Superclass"

To better illustrate multiple inheritance in action, here is some code for you to try out, showing how you can build a right pyramid (a pyramid with a square base) out of a `Triangle` and a `Square`:

```Python
class Triangle:
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return 0.5 * self.base * self.height

class RightPyramid(Triangle, Square):
  def __init__(self, base, slant_height):
    self.base = base
    self.slant_height = slant_height
    # The slant height is the height from the center of the base of an object (like a pyramid) up its face to the peak of that object.

  def area(self):
    base_area = super().area()
    perimeter = super().perimeter()
    return 0.5 * perimeter * self.slant_height + base_area
```

This example declares a `Triangle` class and a `RightPyramid` class that inherits from both `Square` and `Triangle`.

You’ll see another `.area()` method that uses `super()` just like in single inheritance, with the aim of it reaching the `.perimeter()` and `.area()` methods defined all the way up in the `Rectangle` class

>
> Note: You may notice that the code above isn’t using any inherited properties from the `Triangle` class yet. Later examples will fully take advantage of inheritance from both `Triangle` and `Square`.
>

The problem, though, is that both superclasses (`Triangle` and `Square`) define a `.area()`. Take a second and think about what might happen when you call `.area()` on `RightPyramid`, and then try calling it like below:

```Python
>> pyramid = RightPyramid(2, 4)
>> pyramid.area()
Traceback (most recent call last):
  File "shapes.py", line 63, in <module>
    print(pyramid.area())
  File "shapes.py", line 47, in area
    base_area = super().area()
  File "shapes.py", line 38, in area
    return 0.5 * self.base * self.height
AttributeError: 'RightPyramid' object has no attribute 'height'
```

>
> Note: How did we notice that `Triangle.area()` was called and not, as we hoped, `Square.area()`? If you look at the last line of the traceback (before the `AttributeError`), you’ll see a reference to a specific line of code:
>
> `return 0.5 * self.base * self.height`
>
>You may recognize this from geometry class as the formula for the area of a triangle. Otherwise, if you’re like me, you might have scrolled up to the `Triangle` and `Rectangle` `class` definitions and seen this same code in `Triangle.area()`.
>

Did you guess that `Python` will try to call `Triangle.area()`? This is because of something
called the _method resolution order_.

### Method resolution order

The method resolution order (or `MRO`) tells `Python` how to search for inherited methods. This comes in handy when you’re using `super()` because the `MRO` tells you exactly where Python will look for a method you’re calling with `super()` and in _what order_.

_Every class_ has an `.__mro__` attribute that allows us to _inspect the order_, so let’s do that:

```Python
>>> RightPyramid.__mro__
(<class '__main__.RightPyramid'>, <class '__main__.Triangle'>,
 <class '__main__.Square'>, <class '__main__.Rectangle'>,
 <class 'object'>)
```

This tells us that methods will be searched first in `Rightpyramid`, then in `Triangle`, then in `Square`, then `Rectangle`, and then, if nothing is found, in object, from which all classes originate.

The problem here is that the interpreter is searching for `.area()` in `Triangle` _before_ `Square` and `Rectangle`, and upon finding `.area()` in `Triangle`, `Python` calls it _instead of the one you want_. Because `Triangle.area()` expects there to be a `.height` and a `.base` attribute, `Python` throws an `AttributeError`.

Luckily, you have some control over how the `MRO` is constructed. Just by changing the signature of the `RightPyramid` class, you can search in the order you want, and the methods will resolve correctly:

```Python
class RightPyramid(Square, Triangle):
  def __init__(self, base, slant_height):
    self.base = base
    self.slant_height = slant_height
    super().__init__(self.base)

  def area(self):
    base_area = super().area()
    perimeter = super().perimeter()
    return 0.5 * perimeter * self.slant_height + base_area
```

Notice that `RightPyramid` initializes partially with the `.__init__()` from the `Square` class. This allows `.area()` to use the `.length` on the object, as is designed.

Now, you can build a pyramid, inspect the `MRO`, and calculate the surface area:

```Python
>>> pyramid = RightPyramid(2, 4)
>>> RightPyramid.__mro__
(<class '__main__.RightPyramid'>, <class '__main__.Square'>,
<class '__main__.Rectangle'>, <class '__main__.Triangle'>,
<class 'object'>)
>>> pyramid.area()
20.0
```

You see that the `MRO` is now what you’d expect, and you can inspect the area of the pyramid as well, thanks to `.area()` and `.perimeter()`.

_There’s still a problem here, though._ For the sake of simplicity, I did a few things wrong in this example: the first, and arguably most importantly, was that I had two separate classes with the same method name and signature.

This causes issues with method resolution, because the first instance of `.area()` that is encountered in the `MRO` list will be called.

When you’re using `super()` with multiple inheritance, it’s imperative to design your classes to cooperate. Part of this is _ensuring that your methods are unique_ so that they get resolved in the `MRO`, by making sure _method signatures are unique_—whether by using method names or method parameters.

In this case, to avoid a complete overhaul of your code, you can rename the `Triangle` class’s `.area()` method to `.tri_area()`. This way, the area methods can continue using class properties rather than taking external parameters:

```Python
class Triangle:
  def __init__(self, base, height):
      self.base = base
      self.height = height
      super().__init__()

  def tri_area(self):
      return 0.5 * self.base * self.height
```

Let’s also go ahead and use this in the `RightPyramid` class:

```Python
class RightPyramid(Square, Triangle):
  def __init__(self, base, slant_height):
    self.base = base
    self.slant_height = slant_height
    super().__init__(self.base)

  def area(self):
    base_area = super().area()
    perimeter = super().perimeter()
    return 0.5 * perimeter * self.slant_height + base_area

  def area_2(self):
    base_area = super().area()
    triangle_area = super().tri_area()
    return triangle_area * 4 + base_area
```

The next issue here is that the code doesn’t have a delegated `Triangle` object like it does for a `Square` object, so calling `.area_2()` will give us an AttributeError since `.base` and `.height` don’t have any values.

You need to do two things to fix this:

1. All methods that are called with `super()` need to have a call to their superclass’s version of that method. This means that you will need to add `1super().__init__()` to the `.__init__()` methods of Triangle and Rectangle.
2. Redesign all the `.__init__()` calls to take a keyword dictionary. See the complete code below.

```Python
class Rectangle:
  def __init__(self, length, width, **kwargs):
      self.length = length
      self.width = width
      super().__init__(**kwargs)

  def area(self):
      return self.length * self.width

  def perimeter(self):
      return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from
# the Rectangle class
class Square(Rectangle):
  def __init__(self, length, **kwargs):
      super().__init__(length=length, width=length, **kwargs)

class Cube(Square):
  def surface_area(self):
    face_area = super().area()
    return face_area * 6

  def volume(self):
    face_area = super().area()
    return face_area * self.length

class Triangle:
  def __init__(self, base, height, **kwargs):
    self.base = base
    self.height = height
    super().__init__(**kwargs)

  def tri_area(self):
    return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
  def __init__(self, base, slant_height, **kwargs):
    self.base = base
    self.slant_height = slant_height
    kwargs["height"] = slant_height
    kwargs["length"] = base
    super().__init__(base=base, **kwargs)

  def area(self):
    base_area = super().area()
    perimeter = super().perimeter()
    return 0.5 * perimeter * self.slant_height + base_area

  def area_2(self):
    base_area = super().area()
    triangle_area = super().tri_area()
    return triangle_area * 4 + base_area
```

There are a number of important differences in this code:

>
>`**kwargs` is modified in some places (such as `RightPyramid.__init__()`):`**` This will allow users of these objects to instantiate them only with the arguments that make sense for that particular object.
>
> Setting up named arguments before `**kwargs:` You can see this `in RightPyramid.__init__()`. This has the neat effect of popping that key right out of the `**kwargs` dictionary, so that by the time that it ends up at the end of the MRO in the object class, `**kwargs` is empty.

Now, when you use these updated classes, you have this:

```Python
>>> pyramid = RightPyramid(base=2, slant_height=4)
>>> pyramid.area()
20.0
>>> pyramid.area_2()
20.0
```

It works! You’ve used `super()` to successfully navigate a complicated class hierarchy while using both inheritance and composition to create new classes with minimal reimplementation.

## Multiple inheritance alternatives

... Ask me if you want some notes but it involves

- composition
- `mixins`

---

## Some final thoughts on super() and OOP in Python

Here we learned how to supercharge your classes with `super()`. Your journey started with a review of single inheritance and then showed how to call superclass methods easily with `super()`.

You then learned how `multiple inheritance` works in `Python`, and techniques to combine `super()` with `multiple inheritance`. You also learned about how `Python` resolves `method` calls using the _method resolution order_ (`MRO`), as well as how to inspect and modify the MRO to ensure appropriate methods are called at appropriate times.

### Other thoughts

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

---
