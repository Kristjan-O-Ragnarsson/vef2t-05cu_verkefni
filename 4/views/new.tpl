<!DOCTYPE html>
<html>
% include('headder.tpl')
% include('menu.tpl')
	<center><h1>{{title}}</h1></center><hr>
	<div>
		<h2>{{author}}</h2>
		<center>
% try:
		<img src="/static/img/{{img}}">
% except NameError:
		<img src="/static/img/news.jpg">
%end
		</center>
		<br>
		{{content}}
	</div>
% include('fotter.tpl')
</html>