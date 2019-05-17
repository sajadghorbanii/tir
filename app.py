import os
from bottle import route, run, request
import subprocess
from ansi2html import ansi2html


@route('/hello/:name')
def test(name='World'):
    return '<b>Hello %s!</b>' % name
@route('/')
def index():
	#html=subprocess.call(['python3','ti.py'])
	if os.path.exists("data"):
		os.remove("data")
	done=os.system("python3 ti.py >> data")
	with open('data', 'r') as myfile:
		html = myfile.read()
	if request.environ.get('HTTP_USER_AGENT').strip().startswith("curl"):
		return html


	style='''
	<style>
		body{
			color: #f1f5c8;
			background: #222121;
		}
		pre {
			width: 100%;
			padding: 0;
			margin: 0;
			overflow: auto;
			overflow-y: hidden;
			font-size: 12px;
		}
		pre code {
			padding: 0px;
			color: #333;
		}
	</style>
	'''


	html = ansi2html(html)
	html2=html.split("\n")
	html3=""
	for line in html2:
		html3=html3+"<pre>" + line + "</pre>\n" 
	html=html.replace("\n","<br>")
	return style+html3.replace("002B36","1E5866")

port = os.environ.get('PORT', 5000)
run(host='0.0.0.0', port=port)
