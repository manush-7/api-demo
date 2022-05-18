
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container">
  <div class="row">
    <div class="col-sm-12">
      <h3>Column 1</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
  </div>
</div>
<script>
    var data = window.location.href;
var parameter = data.split("#");
var res = parameter[1].split("&");
var tokenData = res[0].split("id_token=")[1];
console.log("tokenData", tokenData);
    $.ajax({
    url: "https://3fzkedpbb1.execute-api.us-west-2.amazonaws.com/dev/rdstos3?date=test",
    headers: {"Authorization": "Bearer " + tokenData},
    crossDomain: true,
          contentType:'application/json',
          secure: true,
    type: "GET",
    success: function(data){
    console.log('data', data);
  }
});

$.ajax({
          url: "https://3fzkedpbb1.execute-api.us-west-2.amazonaws.com/dev/rdstos3?date=test",
          type: 'GET',
          cors: false,
          contentType:'application/json',
          secure: true,
          crossDomain: true,
          headers: {
            'Access-Control-Allow-Origin': '*',
          },
          beforeSend: function (xhr) {
            xhr.setRequestHeader ("Authorization", "Bearer " + tokenData);
          },
          success: function (data){
            console.log(data);
          }
      })
</script>
</body>
</html>
