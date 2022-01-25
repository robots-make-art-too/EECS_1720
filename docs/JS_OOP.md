# JavaScript OOP[^1]

	- [O]bject [O]riented [P]rogramming


##### Still updating this file...



## Quick Introduction to JavaScript

1. JavaScript is a lightweight, cross-platform, and interpreted scripting language. 
	 - lightweight:
 	 - cross-platform:
	 - interpreted:
	 - scripting:

> FYI HTML: [H]yper [T]ext [M]arkup [L]anguage
> FYI CSS: [C]ascading [S]tyle [S]heets

So, _usually_ you can think of HTML as content structure, CSS as content appearance, and JavaScript as content behaviour. But this is changing(confusion inevitable).

#### **If we want anything to change on a webpage without reloading the entire page, we need JavaScript** [help me](https://css-tricks.com/why-javascript-is-eating-html/)[^2]

##### [this]((https://css-tricks.com/why-javascript-is-eating-html/) is also useful in clarifying `imperative` v `declarative` programming... 
	
###### and it is _PROBABLY USEFUL FOR UNDERSTANDING THE HOWS AND WHATS BEHIND YOUR BROWSER EXTENSION_

2. It is well-known for the development of web pages... but many non-browser environments also use it.
	 - Get used to the word(s) `API`s
		 - [A]pplication [P]rogramming [I]nterface
		 - EECS 1720 anyone?: _Building_ _Interactive_ _Systems_

3. JavaScript is a dynamic language.
	 - So? Each Javascript component is dynamic all the way from individual variables to the code itself. 

4. WOW. With the help of JavaScript, you can:
	 - Create variables on-the-go (during `runtime`)
	 - Change their data-type
	 - Create new functions
	 - Replace existing logic

		**Result:**

> I totally know JavaScript: 
	- performs like the best programming language ever

> I thought Java was short for JavaScript: 
	- why do I get different random errors for the SAME LINE OF CODE!!!!!!!!!

This random behavior can _and will_ build up certain complexities... in our case?  **Especially** if using it in a project. A shared Group Project. With different files. And different ~~styles~~. No. We will `use strict` and follw `EC`


### What is JavaScript used for?

- server side: allows interacting
- client side: how we interact with
	- from client to server: `Node.js` is the best! (this is _debatable_ (not really) but it's what we will use... because... it is what I use ^.^ (and it is powerful server-side))
- what else?
	- art: `p5.js` (we use it)
	- machine learning: `ml5.js` (you might use it)

### How can we use JavaScript?

- internal JS: into the html `<script>` between tags `</script>`
	- `<head>` **here** `</head>` _or_ `<body>` **here** `</body>`
- external JS: link to separate file as an `extension.js`
	- `<head>` **usually here** `</head>`


## JavaScript: Standard Form

### Syntax
```JavaScript
	<script type="text/javascript">
	    // Your javaScript code
	</script>

```

### Characteristics of JavaScript

1. Dynamically typed
	 - accepts different data types over time
2. Case Sensitive Format
	 - CASe SeNSitivE != case sensitive
3. Light Weight
   - ? used everywhere a.k.a JavaScript is the support for all browsers
4. Event Handling (includes `throwing` errors and `catching` them)
	 - We could summarise a website as: a series of handled events, anticipated or not.
	 - Can we make _only_ HTML websites? (yes but) 
5. Interpreter Centered
	 - We can get output _without_ using the compiler 


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
		<h2>JavaScript in Head</h2>
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
3. JavaScript from External Files `external.js`
```JavaScript
	<!DOCTYPE html>
	<html>
	<center>
		<body>
			<h2>External JavaScript</h2>
			<p id="demo">Building Interactive Systems</p>
			<button type="button" onclick="myExternalFunction()">Try it</button>
			<script src="external.js"></script>
		</body>
		<center>
</html>
```

### Benefits of External JavaScript

1. Cached JavaScript files can speed up page loading
	 - SO? Load these and decide:
		 1. [slow](https://www.dollartree.com/)
		 2. [fast]
2. Separate HTML and JavaScript code
	 - SO? Easier to read and maintain


## Strict Mode

### What is this?

### Syntax

"use strict";
```
	"use strict"; // Turn on strict mode.

	myVariable = 1;
```
Output:
```
	Uncaught ReferenceError: a is not defined
```
Example:
```
	"use strict"; // Turn on strict mode.
	let myVariable = 1;
	delete myVariable; 
```
Output: 
```
Uncaught SyntaxError: Delete of an unqualified identifier in strict mode

```
#### JavaScript provides the functionality where you can define a property of an object as deletable that qualifies the property to be deleted in strict mode.


### Key Features of `Strict` Mode

1. Useful when dealing with `local` v `global` variables. 
	- Why? In JavaScript objects are variables: requires the keyword  ~~`var`~~, `let`, or `const` to define one - and you **need** to define them!
	- Recall: `Uncaught ReferenceError: myVariable is not defined`
	- ~~`var`~~ is outdated but you may still use it or come across it
2. Useful when handling deletions.
	- Why? JavaScript provides the functionality where you can define a property of an object as _deletable_.
	- So? This qualifies the property to be deleted in strict mode
	- Recall: `Uncaught SyntaxError: Delete of an unqualified identifier in strict mode`
3. Enforcing reserved `keywords` 


## Functions

A function is a set of statements that take inputs, do some specific computation(s), and produces output. 
All functions:
- start with the keyword `function`
- followed by a uniquely chosen name `funtion uniqueName`
- list of parameters `function uniqueName(param1, param2)`
- enclosed statements with curlies.. `function uniqueName(param1, param2) { \\statements }`

### Syntax
```
function functionName(Parameter1, Parameter2, ..)
{
    // Function body
}
```

### Defining the Function
```
function calcAddition(number1, number2)
{
    return number1 + number2;
}
```

### Calling the Function with (optional) Parameters
```
functionName(Value1, Value2, ..);

```


### Returning Information

A function can (but is not required) to return some values using the keyword `return`
- basic syntax statment: `return value;`


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
```
Output:
```
	The name of the person is Git Hub

	6789
```
Note: Git comes from returning ${person.first_name}; Hub comes from returning ${person.last_name}
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
```
Output: 
```
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
```
Output: 
```
	My name is 1720. Am I studying?: true

```

## Classes

Templates vs Instances == Classes vs Objects

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
```
Output:
```
	Hayabusa

	Kawasaki

	The name of the bike is Hyabusa.
```
2. Traditional
`code`


## Encapsulation

The process of wrapping property and function within a single unit is known as encapsulation. 
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
```
Output:
```
	Name is Git, Address is: YorkU

```

## Inheritence

1. Concept: some, one, or all `property` and/or `method` of an Object is being used by another Object.
2. _Unlike_ (most) OOP languages where _classes inherit classes_, in JavaScript an _Object inherits Object_ 
- certain features (`property` and `method`) of one object can be _reused_ by other `Objects`. 


### Example

`code`
1. Difference to other OOP Languages
2. Method Overriding


##### [^1]: Thanks to [gfg](geeksforgeeks.org) for the helpful JavaScript information

##### [^2]: Also thanks to this [Mike](https://css-tricks.com/why-javascript-is-eating-html/) for general HTML, CSS, JS, HTML-in-JS, JS-in-HTML, and other things you'll probably want to read