<!DOCTYPE html>
<html>
<head>
	<title>Json - for image looping in python</title>
	<style type="text/css">
		div{
			display: inline-block;
			margin: 5px;
			border: red solid 2px;
			min-width: 250px;
		}
	</style>
</head>
<body>
	<h1>{{head}}</h1>
	<a href="/modify">Bætavið mynd</a><br>
% for i in myndir:
	<div>
		<img src="/img/{{i}}">
		<h3>{{i[:-4]}}</h3>
	</div>
	<br>
% end
</body>
</html>