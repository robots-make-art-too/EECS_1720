
# JavaScript OOP |  [O]bject [O]riented [P]rogramming

 (Still updating this file...)

---

## Quick Introduction to JavaScript

1. JavaScript is a lightweight, cross-platform, and interpreted scripting language.
   - lightweight: low memory usage
   - cross-platform: can run on multiple frameworks, operating systems, machine architecture[^1].
   - interpreted: debugging at run-time, can be modified while running, code is evaluated line-by-line
   - scripting: no scope, connects one language to another
     - scripting languages are a subset of programming languages (all scripting languages are programming languages but not all programming languages are scripting languages)
     - markup languages are presentational and a different _kind_ of language (such as HTML, CSS, and our `.md` files written in [m]ark[d]own)
2. It is well-known for the development of web pages... but many non-browser environments also use it.
   - Get used to the word(s) `API`s
     - [A]pplication [P]rogramming [I]nterface
     - EECS 1720 anyone?: _Building Interactive Systems_
3. JavaScript is a dynamic language.
   - So? Each Javascript component is dynamic all the way from individual variables to the code itself.
4. WOW. With the help of JavaScript, you can:
   - Create variables on-the-go (during `runtime`)
   - Change their data-type
   - Create new functions
   - Replace existing logic

> **Result:**
>
> I totally know JavaScript: performs like the best programming language ever
>
> I thought Java was short for JavaScript: why do I get different random errors for the SAME LINE OF CODE!!!
>

This random behavior can _and will_ build up certain complexities... in our case?  **Especially** if using it in a project.  A shared Group Project.  With different files.  And different ~~styles~~.

No. We will use `strict` and follow `ES6` ([what is this?](https://www.educba.com/what-is-es6/))

 FYI:
  HTML: [H]yper [T]ext [M]arkup [L]anguage
  CSS : [C]ascading [S]tyle [S]heets

So, _usually_ you can think of HTML as content structure, CSS as content appearance, and JavaScript as content behaviour. But this is changing (confusion inevitable).
**If we want anything to change on a webpage without reloading the entire page, we need JavaScript** [help me](https://css-tricks.com/why-javascript-is-eating-html/)... that link is also useful in clarifying `imperative` v `declarative` programming... and it is _PROBABLY USEFUL FOR UNDERSTANDING THE HOWS AND WHATS BEHIND YOUR BROWSER EXTENSION_

---

### What is JavaScript used for?

- server side: allows interacting
- client side: how we interact with
  - from client to server: `Node.js` is the best! (this is _debatable_ (not really) but it's what we will use... because... it is what I use ^.^ (and it is powerful server-side))
- what else?
  - art: `p5.js` (we use it)
  - machine learning: `ml5.js` (you might use it)

### How can we use JavaScript?

- internal JavaScript: into the html `<script>` between tags `</script>`
  - `<head>` **here** `</head>` _or_ `<body>` **here** `</body>`
- external JavaScript: link to a separate file as an `extension.js`
  - `<head>` **usually here** `</head>`

---

## JavaScript: Standard Form

### Standard Syntax

```JavaScript
<script type="text/javascript">
  // Your javaScript code
</script>
```

### Characteristics of JavaScript

1. Dynamically typed
   - accepts different data types over time
2. Case sensitive format
   - CASe SeNSitivE != case sensitive
3. Lightweight
   - ? used everywhere a.k.a JavaScript is the support for all browsers
4. Event handling (includes `throwing` errors and `catching` them)
   - We could summarise a website as: a series of handled events, anticipated or not.
   - Can we make _only_ HTML websites? (yes but...)
5. Interpreter centered
   - We can get output _without_ using the compiler

---

### JavaScript in an HTML Document

1. JavaScript in `<head>

    ```HTML
    <!DOCTYPE html>
    <html>
      <head>
        <script type="text/javascript">
          function interact() {
            document.getElementById("demo").innerHTML="Welcome to Building Interactive Systems";
          }
        </script>
      </head>
      <body>
        <h2>JavaScript in Head</h2>
        <p id="demo" style="color:green;">Is Interactive?</p>
        <button type="button" onclick="interact()">Click it</button>
      </body>
    </html>
    ```

2. JavaScript in `<body>`

    ```HTML
    <!DOCTYPE html>
    <html>
      <center>
        <body>
          <h2>JavaScript in Body</h2>
          <p id="demo">Is Interactive?</p>
          <button type="button" onclick="interact()">Try it</button>
          <script type="text/javascript">
            function interact() {
              document.getElementById("demo").innerHTML="Welcome to Building Interactive Systems";
            }
          </script>
        </body>
      </center>
    </html>
    ```

3. JavaScript from External Files `external.js`

    ```HTML
    <!DOCTYPE html>
    <html>
      <center>
        <body>
          <h2>External JavaScript</h2>
          <p id="demo">Is Interactive?</p>
          <button type="button" onclick="interact()">Push it</button>;
          <script type="text/javascript" src="external.js"></script>
        </body>
      </center>
    </html>
    ```

---

### Benefits of External JavaScript

1. Cached JavaScript files can speed up page loading. Want to know more?[^2]
   - [what exactly is website speed?](https://www.websitebuilderexpert.com/building-websites/website-load-time-statistics/)
   - So? Load these and decide (hint: open b after a... is a still loading?):
     1. [slow](https://www.dollartree.com/)
     2. [fast](https://www.amazon.com/)
2. Separate HTML and JavaScript code
   - So? Easier to read and maintain

---

## Strict Mode

### What is this?

`Strict` mode can be enabled providing a set of restrictions that make your JavaScript code much more secure and helps you to maintain a high standard of coding. The JavaScript codes can now be optimized before execution by the engine.

Also known as `strict mode pragma`, `strict` _has its own scope_ and can affect _the whole file_ or _individual methods_

Something to note: our `JSON` files are a type of re-`strict`-ed form (of an ECMAScript literal. **_a what?_** a `literal` refers to a value's notation in code. We often see `string literals` in the format: "this is a string". Here, the `literal` indicates that a string's value is notated by double quotations `" "`)

### How to use `strict`?

Just include the following where relevant (whole file? individual method?)

```JavaScript
"use strict";
```

### What are some of the syntax and logical errors prevented?

1. Auto-global variable declaration

   what?

   **Remember me**:  if you mistakenly use a variable without its definition, JavaScript doesn’t throw an error instead it _declares the variable in global scope which often leads to randomness and undesired outputs_

   Example:

   ```JavaScript
   "use strict"; // Turn on strict mode.
   myVariable = 1;
   ```

   Output:

   ```console
   Uncaught ReferenceError: myVariable is not defined
   ```

2. Duplication of parameter names

   what?

   **Remember me**: JavaScript allows duplicate parameter names, we can prevent this using `strict`

   Example:

   ```JavaScript
   "use strict"; // Turn on strict mode.
   let eval = 5;
   ```

   Output:

   ```console
   Uncaught SyntaxError: Unexpected eval of arguments in strict mode
   ```

3. Using reserved keywords as variable names

   what?

   **Remember me**: JavaScript allows reserved keywords to be used as variable names! WHAT! Enable `strict` if you need to control this nonsense.

   Example:

   ```JavaScript
   "use strict"; // Turn on strict mode.
   let eval = 5;
   ```

   Output:

   ```console
   Uncaught SyntaxError: Unexpected eval or arguments in strict mode
   ```

4. Deletion of JavaScript elements

   what?

   **Remember me**: in strict mode scopes are static and don't change over the lifetime. Deleting variables or functions _is not allowed_ (but it is in regular mode)

   Example:

   ```JavaScript
   "use strict"; // Turn on strict mode.
   let myVariable = 1;
   delete myVariable;
   ```

   Output:

   ```console
   Uncaught SyntaxError: Delete of an unqualified identifier in strict mode
   ```

...(what is unqualified?)

### Key Features of `Strict` Mode

1. Useful when dealing with `local` v `global` variables.
   - Why? In JavaScript objects are variables: requires the keyword  ~~`var`~~, `let`, or `const` to define one (and you **need** to define them!)
   - Recall: `Uncaught ReferenceError: myVariable is not defined`
   - ~~`var`~~ is outdated but you may still use it or come across it

2. Useful when handling deletions.
   - Why? JavaScript provides the functionality where you can define a property of an object as _deletable_.
   - So? This qualifies the property to be deleted in strict mode
   - Recall: `Uncaught SyntaxError: Delete of an unqualified identifier in strict mode`

3. Enforcing reserved `keywords`

---

## Functions

A function is a set of statements that takes input(s), does some specific computation(s), and produces output.

All functions*:

- start with the keyword: `function`
- followed by a uniquely chosen name: `funtion uniqueName`
- list of parameters: `function uniqueName(param1, param2)`
- enclosed statements with curlies..: `function uniqueName(param1, param2) { \\statements }`

  *All for our puposes at this time

### General Function Syntax

```JavaScript
function functionName(Parameter1, Parameter2, ..)
{
  // Function body
}
```

### How do we use Functions?

1. Defining the Function

   Before we can use a function, we have to... define it. All function definitions follow the same basic format. _Remember the `external.js` file?_ That file is just three lines, a function definition, like this one:

   ```JavaScript
   function calcAddition(number1, number2)
   {
     return number1 + number2;
   }
   ```

2. Calling the Function with (optional) Parameters

   `Calling` a function means we want to _use_ it (probably now-ish). If we _defined the function with parameters_, now is a good time to include those:

    ```JavaScript
    functionName(Value1, Value2, ..);
    ```

3. Returning Information

   A function can (but is not required) to return some values using the keyword `return`
   - basic syntax statment: `return value;`

---

# Features of an OOP

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
