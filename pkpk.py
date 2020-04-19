import os
from bottle import route, run
import subprocess


from ansi2html import ansi2html
with open('data', 'r') as myfile:
	html = myfile.read()
	html = ansi2html(html)

	html2=html.split("\n")

	html3=""
	for line in html2:
		html3=html3+"<pre>" + line + "</pre><br>" 
	html=html.replace("\n","<br>")
print( html3 )