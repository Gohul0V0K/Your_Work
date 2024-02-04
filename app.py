from flask import Flask,render_template,jsonify,request
from database import load_jobs,load_job_db,add_application,add_job

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

@app.route("/job/<id>/apply")
def apply_to_job(id):
  jobs=load_job_db(id)
  return render_template('applicationform.html',job=jobs)


@app.route("/job/submited", methods=['POST'])
def application_submited():
  data=request.form
  add_application(data)
  
  return render_template('application_submitted.html',data=data)


@app.route("/newjob")
def new_job():
  return render_template('newjob.html')


@app.route("/newjob/submitted", methods=['POST'])
def job_submited():
  data=request.form
  add_job(data)
  
  return render_template('newjob_submitted.html',data=data)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)