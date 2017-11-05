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
  	# RETURN ALL RESTAURANTS IN DATABASE
  	#restaurants = session.query(Restaurant).all()
  	#return jsonify(restaurants = [i.serialize for i in restaurants])

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

    #return jsonify({'results':meanings})

    ##if restaurant_info != "No Restaurants Found":
    ##  restaurant = Restaurant(restaurant_name = unicode(restaurant_info['name']), restaurant_address = unicode(restaurant_info['address']), restaurant_image = restaurant_info['image'])
    ##  session.add(restaurant)
    ##  session.commit() 
    ##  return jsonify(restaurant = restaurant.serialize)
    ##else:
    ##  return jsonify({"error":"No Restaurants Found for %s in %s" % (mealType, location)})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	