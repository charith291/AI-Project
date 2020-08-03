import clipboard

from flask import Flask,render_template
from flask import request
from flask import jsonify

fromhtr import recognize

b=""

app = Flask(__name__)

@app.route('/')
def index():
returnrender_template('frontend.html')

@app.route('/out/',methods=['GET'])
def out():
	input=str(request.args.get('input'))
	global b
	b=recognize(input)
	returnrender_template('index.html',output=b)

@app.route('/savfil/')
defsavfil():
	f=open("output.txt","a");
	f.write(b)
	f.write("\n>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<\n")
	f.close()
	returnrender_template('index.html',output=b)

@app.route('/coptext/')    
defcoptext():
clipboard.copy(b)
returnrender_template('index.html',output=b)

	
if __name__ == '__main__':
app.run()
