from flask import Flask, jsonify, request
import songcrawler
import json

app = Flask(__name__) 
  
 
@app.route('/')
def welcome():
  return "Welcome to this test project"

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
    return data

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')	