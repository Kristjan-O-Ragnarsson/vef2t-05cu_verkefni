<!DOCTYPE html>
<html>
<head>
	<title>ADMIN</title>
</head>
<body>
	<form action="{{action}}" method="post">
		<fieldset>
			<legend><h1>Log In</h1></legend>
			<label>Username:</label><input type="text" name="username" value="{{username}}"><br>
			<label>Password:</label><input type="password" name="password" value="{{password}}"><br>		
			<input type="submit" value="Submit"/>
			</fieldset>
	</form>
</body>
</html>