import subprocess
from flask import Flask, jsonify, render_template, request
from time import sleep
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/nmap")
def nmap():
	process = subprocess.Popen(['nmap','-sP',"10.120.71.*"], stdout=subprocess.PIPE)
	returned = process.stdout.read().strip()
	return render_template('nmap.html',returned=returned)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
