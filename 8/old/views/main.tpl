<!DOCTYPE html>
<html>
<head>
	<title>{title}</title>
	<style type="text/css">
		div{
			border: black solid 1px;
		}
		a{
			color: black;
		}
	</style>
</head>
<body>
% for i in wares.items():
	<a href="/s/{{i[0]}}">
		<div>
			<center><h2>{{i[1]['item']}}</h2>
			<h3>{{i[1]['h']}}</h3></center>
		</div>
	</a>
% end
	<a href="/cart">
		<div>
			<center><h2>cart</h2></center>
		</div>
	</a>	

</body>
</html>