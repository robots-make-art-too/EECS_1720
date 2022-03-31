# Quick Introduction to JavaScript

## What is JavaScript

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
