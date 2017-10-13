<!DOCTYPE html>
<html>
<head>
	<title>{{title}}</title>
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
% for i in range(7):
%	if to_cart[i] >= 1:
	<a href="/s/{{i + 1}}">
		<div>
			<center><h2>{{wares[str(i + 1)]['item']}}</h2>
			<h3>{{wares[str(i + 1)]['h']}}</h3>
			<h4>{{to_cart[i]}} stk</h4></center>
			<span><a href="/c/d/{{i + 1}}">Remove 1 stk from cart</a></span>
		</div>	
	</a>
	
% end	

</body>
</html>