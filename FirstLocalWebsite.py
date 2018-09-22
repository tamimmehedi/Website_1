from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
  return "Homepage is here"
@app.route('/about')
def about():
  return "Website content goes here"
if__name__ == "__main__":
  app.run(debug=True)
