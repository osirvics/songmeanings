from flask import Flask, jsonify, request
import songcrawler
import json

app = Flask(__name__) 
  
 
@app.route('/api/meanings')
def puppiesFunctionId(id):
  return "This method will act on the puppy with id %s" % id

@app.route('/api/query', methods = ['GET', 'POST'])
def findSongMeaning():
  if request.method == 'GET':
    h = ""
  	
  elif request.method == 'POST':
  	# MAKE A NEW RESTAURANT AND STORE IT IN DATABASE
    query = request.json.get('song_info')
    print("Recieved query: " + str(query))
    meanings = songcrawler.getFromSongsmeanings(query)
    raw = {
        "results": meanings
        }

    data = json.dumps(raw)
    return data

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	