console.log('background running1');

var currentURL;

chrome.browserAction.onClicked.addListener(function(activeTab){
  currentURL = activeTab.url;
  console.log(currentURL)
});

chrome.browserAction.onClicked.addListener(function() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/json", true);
    console.log("posted")
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = (function() {
      if(xhr.readyState == 4 && xhr.status == 200) {
        alert(xhr.responseText);
      }
    })
    var jsonObject = {"parsedText": currentURL };
    var data = JSON.stringify(jsonObject);
    xhr.send(data);
    // chrome.tabs.executeScript(null, {file: 'post.js'})
  });


  console.log('background running');

