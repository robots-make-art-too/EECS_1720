# EECS 1720 `Extension Starter Pack`

## You probably need to know these

Start here.. what is [DOM](https://www.freecodecamp.org/news/what-is-the-dom-document-object-model-meaning-in-javascript/)??

[Anatomy](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Anatomy_of_a_WebExtension) of an extension?

- (this is firefox but any operating system is related - they all use `manifest.json` and they all need to request `premissions`)

---

## OK but what can I _do_ ?

Does it matter which [Browser](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs)?

### manifest.json

- [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)

- [Chrome](https://developer.chrome.com/docs/extensions/mv3/manifest/)

### Permissions

Best by example? These go together:

1. asking for `activeTab` [permission](https://www.geeksforgeeks.org/how-to-check-if-a-browser-tab-is-currently-active-or-not/?ref=gcse)

2. how to check if a browser tab is currently [active](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)

> This concept carries through to other actions you may be interested in and so need to ask permissions for.

### Namespace! A key difference

Switching browsers? Unsure what works where? See if what you are doing is [incompatible](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Chrome_incompatibilities)?

--- 

## OK so what about other ".js" stuff?

Like... adding [`p5.js`](https://www.geeksforgeeks.org/p5-js-select-function/?ref=lbp) to your extension? (It is like adding your `external.js` file only with many more pre-defined function options for drawing, images, sound etc.)

### Did you want an example of aesthetic + technical?

Maybe this Chris[^1] can help you _think_ about aesthetic [concepts](https://blog.homeforfiction.com/2020/02/20/book-worming-party-literature-meets-drawing/)?

---

## Some _specific_ questions you may be asking?

1. Can I find a use for _the whole `HTML` document_, as a [string](https://www.geeksforgeeks.org/how-to-get-the-entire-html-document-as-a-string-in-javascript/?ref=rp)?

2. Do I need to check if this _JavaScript `Object`_ is a [`DOM`](https://www.geeksforgeeks.org/how-to-check-a-javascript-object-is-a-dom-object/?ref=rp) `Object`?

3. What if I want to do something with _the files_, do I need to know the [file extensions](https://www.geeksforgeeks.org/how-to-get-file-extensions-using-javascript/?ref=gcse)?

4. Can I get a list of Chrome [variables](https://www.geeksforgeeks.org/view-the-list-of-all-variables-in-google-chrome-console-using-javascript/?ref=rp)?

- In general you should be _careful_ with concepts like asking for **ALL OF THE EVERYTHING**
  - if implemented inefficiently... things can freeze!

---
---

[^1]: https://homeforfiction.com/#about
