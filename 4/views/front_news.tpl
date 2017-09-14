% for x in ne:
	<a href="/{{x['p']}}">
	<div>
		<h2>{{x['title']}}</h2>
		<hr>
		<h3>{{x['author']}}</h3>
		{{x['content']}}
	</div>
	</a>
	<br>
%end