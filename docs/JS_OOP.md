# JavaScript OOP 

	- [O]bject [O]riented [P]rogramming


## Quick Introduction

 - server side
 - client side


 - internal JS - into the html 
 - external JS - separate file 

### What


### How

```
	<script>
	  // JavaScript Code
	</script>


<script type="text/javascript">
    // Your javaScript code
</script>

```


## Standard Form


### Syntax


### Characteristics

	1. Dynamically typed 

	2. Case Sensitive Format

	3. 


### JS in HTML Document

1. JavaScript in `<head>`

```JavaScript
	<!DOCTYPE html>
	<html>
	<head>
		<script>
			function interact() {
				document.getElementById("demo").innerHTML = "Welcome to Building Interactive Systems";
			}
		</script>
	</head>
	<body>
		<!--<h2>JavaScript in Head</h2>-->
		<p id="demo" style="color:green;">interactive</p>
		<button type="button" onclick="interact()">click it</button>
	</body>
	</html>
```

2. JavaScript in `<body>`


```JavaScript
	<!DOCTYPE html>
	<html>
	<center>
	    <body>
	        <h2>JavaScript in Body</h2>
	        <p id="demo">Interactive.</p>
	        <button type="button" onclick="interact()">Try it</button>
	        <script>
	            function interact() {
	            document.getElementById("demo").innerHTML = "Welcome to Building Interactive Systems";
	            }
	        </script>
	    </body>
	</center>
	</html>


```


3. JavaScript from External Files `addmore.js`




## Strict Mode




### What is this?


### Syntax
```
	"use strict";

	"use strict"; // Turn on strict mode.

	a = 1;

	Output:

	Uncaught ReferenceError: a is not defined


Ex.

	"use strict"; // Turn on strict mode.
	let a = 1;
	delete a; 

Output: 
Uncaught SyntaxError: Delete of an unqualified identifier in strict mode

>>>  JavaScript provides the functionality where you can define a property of an object as deletable that qualifies the property to be deleted in strict mode.

```

### Key Features

	1. useful when local . Global variables 

	2. Note: In JavaScript objects are variables: requires the keyword ‘let’ or ‘const’ to define one.

	3. Enforcing reserved keywords 





## Functions

? A function is a set of statements that take inputs, do some specific computation, and produces output. 

### Syntax

```
	function functionName(Parameter1, Parameter2, ..)
	{
	    // Function body
	}

	function calcAddition(number1, number2)
	{
	    return number1 + number2;
	}


functionName(Value1, Value2, ..);

```


### Definition


### Calling and Parameters

`code`


### Returning Information







## Features of an OOP

1. Object
2. Classes
3. Encapsulation
4. Inheritence


## Object

1. An Object is a unique entity that contains property and methods.

2. The characteristics of an Object are called: Property, in Object-Oriented Programming and the actions are called methods. 

	- What about Methods? NOTE: A Method in javascript is a property of an object whose value is a function. 

3. An Object is an instance of a class. 


### Creating an Object

1. Object Literal

```
	//Defining object
	let person = {
	    first_name: 'Git',
	    last_name: 'Hub',

	    //method
	    getFunction : function(){
	        return (`The name of the person is
	        ${person.first_name} ${person.last_name}`)
	    },

	    //object within object
	    phone_number : {
	        mobile:'12345',
	        landline:'6789'
	        mobile2: 'ffgf'
	    }
	}
	console.log(person.getFunction());
	console.log(person.phone_number.landline);


	Output:
	The name of the person is Git                  Hub
													  ${person.first_name} ${person.last_name}

	6789


```

2. Object Constructor

```
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


	Output: 
	First

	Git Hub

```


3. Object.create() method

```
	// Object.create() example a
	// simple object with some properties

	const coder = {
	    isStudying : false,
	    printIntroduction : function(){
	        console.log(`My name is ${this.name}. Am I
	        studying?: ${this.isStudying}.`)
	    }
	}
	// Object.create() method
	const me = Object.create(coder);

	// "name" is a property set on "me", but not on "coder"
	me.name = '1720';

	// Inherited properties can be overwritten
	me.isStudying = true;

	me.printIntroduction();


	Output: 

	My name is 1720. Am I studying?: true

```


## Classes

	- Templates vs Instances == Classes vs Objects

### Defining a Class

1. ES6

```
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


	Output:

	Hayabusa

	Kawasaki

	The name of the bike is Hyabusa.

```

2. Traditional

`code`


## Encapsulation

1. The process of wrapping property and function within a single unit is known as encapsulation. 

	- Note on alternative meanings

```
	//encapsulation example
	class person{
	    constructor(name,id){
	        this.name = name;
	        this.id = id;
	    }
	    add_Address(add){
	        this.add = add;
	    }
	    getDetails(){
	        console.log(`Name is ${this.name},Address is: ${this.add}`);
	    }
	}

	let person1 = new person('Git',21);
	person1.add_Address('YorkU');
	person1.getDetails();


	Output:
	Name is Git, Address is: YorkU

```


## Inheritence

1.  It is a concept in which some property and methods of an Object is being used by another Object.

2. Unlike most of the OOP languages where classes inherit classes, JavaScript Object inherits Object i.e. certain features (property and methods)of one object can be reused by other Objects. 


### Example

`code`

1. Difference to other OOP Languages

2. Method Overriding