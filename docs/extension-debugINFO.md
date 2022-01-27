# Debug 101

## Rememeber these

1. F12
   - `F12` should default to open `developer` mode in a browser
2. the inspector tool
   - the `inspector` tool (little arrow) allows you to select content and identify common `HTML`, `CSS`, or `JavaScript` tags
3. console.log() _and_ console.dir()
   - `console.log()` and `console.dir()` can display all sorts of useful information that can be executed during `runtime`
   - in _most_ cases `.log()` prints the _`toString` representation of the `Object`_ while `.dir()` recognizes the `Object` and prints _only the `properties`_
4. JSON.stringify()
   - `JSON.stringify()` lets you grab your content in a string format (remember our `JSON` references in lecture?)

If you want to be extra careful loging `Objects`:

> Don't use console.log(obj), use console.log(JSON.parse(JSON.stringify(obj))).
>
> This way you are sure you are seeing the value of obj at the moment you log it. Otherwise, many browsers provide a live view that constantly updates as values change. This may not be what you want. - [MDM Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Console/log#logging_objects)

(but since `console.log(obj)` _could_ give you constantly updating `event triggers`... maybe you could use that for something... like periodic associations to update other content... or?)

### Syntax

 ```JavaScript
 // You could try these for any website
 console.log(document.body);
 console.dir(document.body);
 ```

```HTML
<!DOCTYPE html>
   <html>
      <body>
         <h2>Create JSON string from a JavaScript object.</h2>
         <p id="demo"></p>
         <script>
            // and also try this? let me create an object
            let obj = { "name":"alien plant", "age":679, "city":"that red mountain on Mars"};
            // let me make it a string
            let myJSON = JSON.stringify(obj);
            // now insert the string into an empty paragraph - id="demo"
            document.getElementById("demo").innerHTML = myJSON;
         </script>
      </body>
   </html>
```

Instead of `document.body`, what other `Object` instances might be useful to `inspect`?

- classes
- id
- div
- ?

---

## Couple more questions

What did that _more detailed_ browser extension example do?

1. remove `URL`s
2. change colour of `URL`
3. handle `widgets`
   - twitter
   - side bar
   - maps
   - related searches
   - people also ask
   - ...

### I want more

Don't get overwhelmed, there is a lot going on [here](https://github.com/EECSB/Google-Search-Customizer). If you have **QUESTIONS** just ask!

#### What about?

You should try playing around with `F12`, the `console` _`methods`_, or the `inspector` tool to obtain the `tag` of an `Object` you can alter on a web page!
