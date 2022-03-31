function message(){
   var outputObj = document.getElementById("output");
   var msg = prompt("Please enter a message: ", "");
   outputObj.innerHTML = outputObj.innerHTML + msg + "<hr>";
   msg = msg.replace(/\n/g, "\r\n"); // To retain the Line breaks.

   var blob = new Blob([msg], {type: "text/plain"});
   var anchor = document.createElement("a");
   anchor.download = 'tempfile.txt';
   anchor.href = window.URL.createObjectURL(blob);
   anchor.target = "_blank";
   anchor.style.display = "none";
   document.body.appendChild(anchor);
   anchor.click();
   document.body.removeChild(anchor);
}