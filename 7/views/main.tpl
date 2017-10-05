<!DOCTYPE html>
<html>
<head>
	<title>ADMIN</title>
	<script type="text/javascript">
		alert('með notkun þessarar síðu samðikir þú notkun "cookie" og javascript mining')
	</script>
</head>
<body>
	<form action="{{action}}" method="post">
		<fieldset>
			<legend><h1>Log In</h1></legend>
			<label>Username:</label><input type="text" name="user" value="{{user}}"><br>
			<label>Password:</label><input type="password" name="password" value="{{passw}}"><br>
% if mon:
% include('monero.tpl')
% end			
			<input type="submit" value="Submit"/>
			</fieldset>
	</form>
</body>
</html>