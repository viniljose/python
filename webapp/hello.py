from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return "Hello World from Flask"
app.run()
#http://localhost:5000/    
