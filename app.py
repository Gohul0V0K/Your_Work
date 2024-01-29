from flask import Flask,render_template

app=Flask(__name__)

Jobs=[
  {
    "id":1,
    "title":"Data Analyst",
    "location":"Bengaluru, India",
    "salary":"Rs. 10,00,000"
  },
  {
    "id":2,
    "title":"Data ",
    "location":"Bengaluru, India",
    "salary":"Rs. 10,00,000"
  },
  {
    "id":3,
    "title":" Analyst",
    "location":"Bengaluru, India"
  },
  {
    "id":4,
    "title":"Data enginner",
    "location":"Bengaluru, India",
    "salary":"Rs. 10,00,000"
  }
]
@app.route("/")
def hello():
  return render_template("home.html",jobs=Jobs)
  



if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)