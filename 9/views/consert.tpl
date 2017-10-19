<!DOCTYPE html>
<html>
<head>
	<title>Conserts in iceland</title>
	<style type="text/css">
		*,
		*:before,
		*:after {
		  -webkit-box-sizing: border-box;
		     -moz-box-sizing: border-box;
		          box-sizing: border-box;
		}
		body{
			padding: 25px;
			background: lightgray;
		}
		div{
			float: left;
			padding: 3px;
			display: inline-block;
			margin: 5px;
			border: red solid 2px;
			width: 300px;
			height: 500px;
		}
		article{
			width: 1024px;
			margin: auto;
		}

	</style>
</head>
<body>
	<center><h1><strong>Conserts in iceland</strong></h1></center>
<article>
% for i in results:
	<div>
		<center><h3>{{i['eventDateName']}}</h3></center>
		<img src="{{i['imageSource']}}">
		<h4>{{i['eventHallName']}}</h4>
		<h4>{{i['dateOfShow']}}</h4>
		<h4>{{i['userGroupName']}}</h4>
	</div>
% end
</article>
</body>
</html>