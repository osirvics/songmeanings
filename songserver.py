from flask import Flask, jsonify, request
import songcrawler
import json
from redis import Redis
import os

app = Flask(__name__) 
redis = redis.from_url(os.environ['REDISCLOUD_URL'])
#redis = Redis() 
#redis = Redis(host= "redis", port=6379)  
 
@app.route('/')
def welcome():
  return "Welcome to this test project"

@app.route('/hitcount')
def getCount():
  return 'This server has recieved {0} hits' .format(redis.get('hits'))

@app.route('/api/query', methods = ['GET', 'POST'])
def findSongMeaning():
  if request.method == 'GET':
    return "Don't call this endpoint"

  elif request.method == 'POST':
    query = request.json.get('song_info')
    print("Recieved query: " + str(query))
    meanings = songcrawler.getFromSongsmeanings(query)

    raw = {
        "results": meanings
        }

    data = json.dumps(raw)
    redis.incr('hits')
    return data

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')	