# A bit of extra sauce

Since A-Frame is just HTML, we can control the scene and its entities using JavaScript and DOM APIs as we mostly would in ordinary web development.
Every element in the scene, even elements such as <a-box> or <a-sky>, are entities (represented as <a-entity>). A-Frame modifies the HTML element prototype to add some extra behavior for certain DOM APIs to tailor them to A-Frame.
  
Encapsulate your JavaScript code within A-Frame components. Components modularize code, make logic and behavior visible from HTML, and ensure that code is executed at the correct time (e.g., after the scene and entities have attached and initialized). As the most basic example, to register a `console.log` component before `<a-scene>`:
  
```JavaScript
AFRAME.registerComponent('log', {
  schema: {type: 'string'},

  init: function () {
    var stringToLog = this.data;
    console.log(stringToLog);
  }
});
```
_After_ we do the registration, we can use the compoenent from `HTML`:

```HTML
<a-scene log="Hello, Scene!">
  <a-box log="Hello, Box!"></a-box>
</a-scene>
```
_Now_ we can use our browser's Developer Tools Console (hit that `F12` again) to run `JavaScript` on our scene, and to check `console.log` displays!
  
1. [JavaScript events](https://aframe.io/docs/1.3.0/introduction/javascript-events-dom-apis.html)
2. [Run content on screeen](https://aframe.io/docs/1.3.0/core/scene.html#running-content-scripts-on-the-scene)
  
---

When we use `AR` and particularly `GPS` type content, the standard is the enforce `Secure context: This feature is available only in secure contexts (HTTPS), in some or all supporting browsers`. We could use: 

```JavaScript
navigator.geolocation.getCurrentPosition(success, error, [options])
```

Which is implemented here: 

```JavaScript
var options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
};

function success(pos) {
  var crd = pos.coords;

  console.log('Your current position is:');
  console.log(`Latitude : ${crd.latitude}`);
  console.log(`Longitude: ${crd.longitude}`);
  console.log(`More or less ${crd.accuracy} meters.`);
}

function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

navigator.geolocation.getCurrentPosition(success, error, options);
```

---

If the object exists, geolocation services are available. You can test for the presence of geolocation:

```JavaScript
if('geolocation' in navigator) {
  /* geolocation is available */
} else {
  /* geolocation IS NOT available */
}
```

```JavaScript
function success(position) {
  const latitude  = position.coords.latitude;
  const longitude = position.coords.longitude;

  // Do something with your latitude and longitude
}
```
