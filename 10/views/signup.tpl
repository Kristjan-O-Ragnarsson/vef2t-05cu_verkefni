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
	<form action="{{action}}" method="post">
		<fieldset>
			<legend><strong>Sign Up</strong></legend>
			<label>Username:</label><input type="text" name="username" value="{{username}}" pattern="\w+" required><br>
			<label>Password:</label><input type="password" name="password" value="{{password}}" required><br>
			1 number 1 letter 12 min length(not requierd)
			<input type="submit" value="submit">
		</fieldset>
	</form>
	
</body>
</html>