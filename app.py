from flask import Flask,render_template,jsonify
from database import load_jobs,load_job_db

app=Flask(__name__)




@app.route("/")
def hello():
  Jobs=load_jobs()
  return render_template("home.html",jobs=Jobs)
  
@app.route("/job/<id>")
def dynamic_job_page(id):
  try:
    jobs=load_job_db(id)
  except IndexError as e:
    return render_template("404.html")
    
  return render_template('jobpage.html',job=jobs)


if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)