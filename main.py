from flask import Flask, request

app = Flask(__name__)

@app.route('/robot', methods=["POST"])
def robot():
  form = request.form
  if form['metal'] == 'Yes':
    return "You're a robot"
  elif "error" in form["captcha"].lower():
    return "You're a robot"
  elif form["food"] == "synthetic oil" :
    return "You're a robot"
  else:
    return "Welcome Fellow Human 🗿"
@app.route('/')
def login_user():
  page = ""
  f = open("static/days.html","r")
  page = f.read()
  f.close()
  return page
app.run(host='0.0.0.0', port=81)