
# JavaScript OOP |  [O]bject [O]riented [P]rogramming

## Features of an OOP

1. Object
2. Classes
3. Encapsulation
4. Inheritence

---

## Object

1. An `Object` is a unique entity that contains `Property` and `Method`
2. The _characteristics_ of an `Object` are properties
3. The _actions_ of an `Object` are methods
   - NOTE: A `Method` in JavaScript
     - is a `Property` of an `Object`
       - whose `Value` is a `Function`
4. An Object is an _instance_ of a `Class`

psst: pretty much everything is an Object in JavaScript (yes, even functions, arrays, and strings!)

### How can we create an Object?

1. Object Literal

   ```JavaScript
   //Defining the object
   let person = {
     first_name: 'Git',
     last_name: 'Hub',

     //a useful method
     getFunction : function(){
       return (`The name of the person is ${person.first_name} ${person.last_name}`)
     },

     //we can have an object within an object
     phone_number : {
       mobile:'12345',
       landline:'6789',
       mobile2: 'ffgf'
     }
   }

   console.log(person.getFunction());
   console.log(person.phone_number.landline);
   ```

   Output:

   ```console
   The name of the person is Git Hub
   6789
   ```

   Note:
   - The returned value 'Git' comes from returning `${person.first_name}`
   - `phone_number.mobile` and `phone_number.mobile2` are both accepted as `numbers` and `letters`

2. Object Constructor

   The `this`.

   ```JavaScript
   //using a constructor
   function person(first_name,last_name){
     this.first_name = first_name;
     this.last_name = last_name;
   }

   //creating new instances of person object
   let person1 = new person('First','Last');
   let person2 = new person('Git','Hub');

   console.log(person1.first_name);
   console.log(`${person2.first_name} ${person2.last_name}`);
   ```

   Output:

   ```console
   First
   Git Hub
   ```

3. Object.create() method

   This creates a new object by using an existing object as the prototype of the newly created object.

    ```JavaScript
    // Object.create() example
    // a simple object with some properties

    const coder = {
      isStudying : false,
      printIntroduction : function(){
        console.log(`My name is ${this.name}. Am I studying?: ${this.isStudying}.`)
      }
    }

    // the Object.create() method
    const me = Object.create(coder);

    // "name" is a property set on "me", but not on "coder"
    me.name = '1720';

    // Inherited properties can be overwritten
    me.isStudying = true;
    me.printIntroduction();
    ```

    Output:

    ```console
    My name is 1720. Am I studying?: true
    ```

**IMPORTANT**: in the example above you should have noticed that:

- our _existing `Object` instance_, called `coder`, has properties and methods `isStudying` and `printIntroduction`
- these are _inherited_ by our _new `Object` instance,_ called `me`
  - (`coder` is the _protoype_ we based our instance `me` on)
- we then give our _new `Object` instance_ a _new property_, called `name`
- our _prototype `Object` instance_ (`coder`) does **not** have a property `name`
  - (but our new instance `me` does...)
  - if we could use our _new `Object` instance_ (`me`) as a prototype... we could make a _new_ new `Object` instance which _would_ inherit the property `name`

---

(HEY! maybe you have noticed how _useful_ `console.log()` is?)

- (Maybe you also noticed how `F12` might solve all problems?)

---

## Classes

1. Classes are like the _blueprint_ of an `Object`
2. A `Class` can have many Objects
   - Why? Because a `Class` is a _template_
3. Objects are instances of the class
   - ? They are the implementation

In other words, Templates are to Instances as Classes are to Objects.

- You can also think of `classes` as _special functions_

---

**WAIT**. _Unlike_ (most) OOP languages there are technically _no_ classes in JavaScript (because... everything is an object).

**INSTEAD** we consider JavaScript to be a _Prototype Based Object Oriented Language_

- behaviours are defined using a constructor function
- behaviours are _reused_ by reusing _existing_ `Objects`
  - this is called _inheritence_

> _The class syntax is not introducing a new object-oriented inheritance model to JavaScript. JavaScript classes provide a much simpler and clearer syntax to create objects and deal with inheritance.
–[Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)_

---

### Defining a Class

The updated `ES6` format for JavaScript implements a JavaScript version of `classes`. Traditionally, `classes` were simulated through `Object` definitions. Let's look at the different formats. Does `ES6` make it easier to define and reuse an `Object`?

1. ES6

   ```JavaScript
   // Defining class using es6
   class Vehicle {
     constructor(name, maker, engine) {
       this.name = name;
       this.maker = maker;
       this.engine = engine;
     }

     getDetails(){
       return (`The name of the bike is ${this.name}.`)
     }
   }

   // Making object with the help of the constructor
   let bike1 = new Vehicle('Hayabusa', 'Suzuki', '1340cc');
   let bike2 = new Vehicle('Ninja', 'Kawasaki', '998cc');

   console.log(bike1.name); // Hayabusa
   console.log(bike2.maker); // Kawasaki
   console.log(bike1.getDetails());
   ```

   Output:

   ```console
   Hayabusa
   Kawasaki
   The name of the bike is Hayabusa.
   ```

2. Traditional

   ```JavaScript
   // Defining class in a Traditional Way
   function Vehicle(name,maker,engine){
     this.name = name,
     this.maker = maker,
     this.engine = engine
   };

   Vehicle.prototype.getDetails = function(){
     console.log('The name of the bike is '+ this.name);
   }

   let bike1 = new Vehicle('Hayabusa','Suzuki','1340cc');
   let bike2 = new Vehicle('Ninja','Kawasaki','998cc');

   console.log(bike1.name);
   console.log(bike2.maker);
   console.log(bike1.getDetails());
   ```

   Output:

   ```console
   Hayabusa
   Kawasaki
   The name of the bike is Hayabusa.
   ```

---

## Encapsulation

The process of _wrapping `property` and `function` within a single unit_ is known as `encapsulation`

Example:

```JavaScript
//an encapsulation example
class person{
  constructor(name,id){
    this.name = name;
    this.id = id;
  }

  add_Address(add){
    this.add = add;
  }

  getDetails(){
    console.log(`Name is ${this.name}, Address is: ${this.add}`);
  }
}

let person1 = new person('Git',21);

person1.add_Address('YorkU');
person1.getDetails();
```

Output:

```console
Name is Git, Address is: YorkU
```

---

Alternatively, `encapsulation` can also refer to _restricting the scope_ of a variable within the `Class` or `Object`

Example:

```JavaScript
// Abstraction example
// we change the scope through the definition format of our function
function person(fname,lname){
  let firstname = fname;
  let lastname = lname;
  
  // how to define a no access version
  let getDetails_noaccess = function(){
    return (`First name is: ${firstname} Last name is: ${lastname}`);
  }
  
  // how to define an accessible version
  this.getDetails_access = function(){
    return (`First name is: ${firstname}, Last name is: ${lastname}`);
  }
}

let person1 = new person('NAME','LAST');

console.log(person1.firstname);
console.log(person1.getDetails_noaccess);
console.log(person1.getDetails_access());
```

Output:

```console
undefined
undefined
First name is: NAME, Last name is: LAST
```

What happened?

- we try to access `property` _person1.firstname_ and `function` _person1.getDetails_noaccess_
- because we changed _how_ we defined the function, we have _restricted the function's scope_
  - we get a return of _undefined_
    - even though we know there is a `method` we can access through our `Object` instance, _person_ (_person1.getDetails_access()_)

---

## Inheritence

1. Concept: some, one, or all `property` and/or `method` of an Object is being used by another Object.
2. _Unlike_ (most) OOP languages where _classes inherit classes_, in JavaScript an _Object inherits Object_
   - certain features (`property` and `method`) of one object can be _reused_ by other `Objects`.

Example:

```JavaScript
//Inheritance example
class person{
  constructor(name){
    this.name = name;
  }

  //method to return the string
  toString(){
    return (`Name of person: ${this.name}`);
  }
}

//we use the super keyword to call the class constructor above
class student extends person{
  constructor(name,id){
    super(name);
    this.id = id;
  }

  toString(){
    return (`${super.toString()},Student ID: ${this.id}`);
  }
}

let student1 = new student('NAME',22);

console.log(student1.toString());
```

Output:

```console
Name of person: NAME, Student ID: 22
```

---

In the example above both `Object` _student_ and `Object` _person_ have the same `Method` _toString()_

- this is called `method overriding`
- `method overriding` allows a `Method` in a _child_ (our `student`) to have the same name as a `Method` in its _parent_ `Class` (our `person`)
  - we use a `keyword` called _super_ to **_refer to the immediate parent class instance variable_**

---
---

### Thanks to [gfg](geeksforgeeks.org) for the helpful JavaScript information

#### Also thanks to this [Mike](https://css-tricks.com/why-javascript-is-eating-html/) for general HTML, CSS, JS, HTML-in-JS, JS-in-HTML, and other things you'll probably want to read

[^1]: https://www.sciencedirect.com/topics/computer-science/computer-architecture

[^2]: https://backlinko.com/page-speed-stats

<https://www.zdnet.com/article/the-fastest-websites-on-the-internet-today/>

<https://financialpost.com/personal-finance/business-essentials/the-coding-industry-in-canada-is-growing-rapidly>
