from supabase import create_client, Client
import os

SUPABASE_URL = my_secret = os.environ['base_url']
SUPABASE_KEY = my_secret = os.environ['base_key']

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def load_jobs():
  result=[]
  response = list(supabase.table('jobs').select("*").execute())
  for i in range(len(response[0][1])-1,-1,-1):
    result.append(response[0][1][i])

  return result

def load_job_db(id):
  columns = '*'
  condition = {'id': id}

  response = list(supabase.table('jobs').select(columns).eq('id', id).execute())

  return response[0][1][0]



def add_application(data):
  data_to_insert=[{
    'job_id':data['job_id'],
    'job_title':data['job_title'],
    'name':data['fullname'],
    'email':data['email'],
    'linked_in_url':data['linkedin']
  }]

   
  response=supabase.table('application').insert(data_to_insert).execute()
  


def add_job(data):
  data_to_insert=[{
    'title':data['title'],
    'location':data['location'],
    'salary':data['salary'],
    'email':data['email'],
    'responsibility':data['responsibility'],
    'requirement':data['requirement']
  }]

  response=supabase.table('jobs').insert(data_to_insert).execute()

