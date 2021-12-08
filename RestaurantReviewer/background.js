chrome.browserAction.onClicked.addListener(function() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/json", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = (function() {
      if(xhr.readyState == 4 && xhr.status == 200) {
        alert(xhr.responseText);
      }
    })
    var review = prompt("Paste review here")
    console.log(review)
    var jsonObject = {"parsedText": review };
    var data = JSON.stringify(jsonObject);
    xhr.send(data);
});