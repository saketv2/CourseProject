<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>

</head>
<body>
  <p id = "serverResponse"></p>
<script>
  const xhr = new XMLHttpRequest();

  //function is called when connection is successful
  xhr.onload = function() {
    const serverResponse = document.getELementById("serverResponse");
    serverResponse.innerHTML = this.responseText;
  }

  xhr.open("POST", "server");
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhr.send("text = Trump is our lord and savior");
  </script>
</body>
</html>