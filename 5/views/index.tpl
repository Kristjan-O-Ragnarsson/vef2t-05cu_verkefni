<!DOCTYPE html>
<html>
<head>
	<title>Pöntunarsíða</title>
</head>
<body>
	<h1>Pizzu pöntunar vélin</h1>
	<form action="/" method="post">
		<fieldset>
			<legend><strong>Pitzur</strong></legend>
			<h2>Upplysingar um notandann</h2>
			<label>Nafnið:</label><input type="text" name="name" required><br>
			<label>Heimilisfang:</label><input type="text" name="address" required><br>
			<label>Netfang:</label><input type="email" name="email" required><br>
			<label>Símanumer:</label><input type="tel" name="tele" pattern="[\+]{0,1}[\354]{0,1}\d{3}[\-]\d{4}" placeholder="112-4455" required><br>
			<h2>Pizzastærð</h2>
			Hvaða stærð má bjóða þér?<br>
			<input type="radio" name="size" value="9"><label>9 tomma - 1000kr.</label><br>
			<input type="radio" name="size" value="12"><label>12 tomma - 1500kr.</label><br>
			<input type="radio" name="size" value="18"><label>18 tomma - 2000kr.</label><br>

			<h2>Val um álegg</h2>
			Hvaða álegg má bjóða þér?
			<br><br>
			Hvert álegg kostar 200kr.<br>
			<input type="checkbox" name="topping[0]" value="Skinka"><label>Skinka</label><br>
			<input type="checkbox" name="topping[1]" value="Annanas"><label>Annanas</label><br>
			<input type="checkbox" name="topping[2]" value="Pepperoni"><label>Pepperoni</label><br>
			<br>
			<input type="submit" value="Skila inn">
		</fieldset>
	</form>
</body>
</html>