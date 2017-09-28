<!DOCTYPE html>
<html>
<head>
	<title>Sign Up</title>
% if villa == 1:
	<script type="text/javascript">
		alert('{{error}}')
	</script>
% end
</head>
<body>
	<form action="/" method="post">
		<fieldset>
			<legend><strong>Sign Up</strong></legend>
			<label>Name:</label><input type="text" name="name" value="{{name}}" required autofocus><br>
			<label>Email:</label><input type="email" name="email" value="{{email}}" required><br>
			<label>Phone:</label><input type="tel" name="tel" value="{{tel}}" pattern="^(\+354)?\d{3}[ -]?\d{4}$" required><br>
			<label>Username:</label><input type="text" name="username" value="{{username}}" required><br>
			<label>Password:</label><input type="password" name="password" value="{{password}}" pattern="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{12,}$" required><br>
			1 number 1 letter 12 min length
			<input type="submit" value="submit">
		</fieldset>
	</form>
	
</body>
</html>