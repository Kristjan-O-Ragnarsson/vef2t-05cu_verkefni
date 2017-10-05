<!DOCTYPE html>
<html>
<head>
	<title>{{title}}</title>
	<script type="text/javascript">
		alert('{{msg}}');
% if succ == 0:
		window.location.replace("/");
% end
	</script>
</head>
<body>
% if succ == 1:
%   include('logout.tpl')
% end
</body>
</html>