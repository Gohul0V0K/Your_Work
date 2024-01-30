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

