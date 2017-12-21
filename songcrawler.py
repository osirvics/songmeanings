import time
import urllib
import bs4
import requests
import startcrawl
import types

def remove_smart_quotes (text):
  return text.replace(u"\u2018", "'") \
             .replace(u"\u2019", "'") \
             .replace(u"\u201c", '"') \
             .replace(u"\u201d", '"')


def getFromSongsmeanings(search_query):
	target_url = startcrawl.findUrl(search_query)
	if target_url is not None:
		response = requests.get(target_url)
		html = response.text
		soup = bs4.BeautifulSoup(html, "html.parser")
		outputList = []
		#commentsHolder = soup.find(class_= "holder-comments")\
		print(soup.find(class_ = "heading_meanings").text)
		commentsList = soup.find(id= "comments-list")	
		comments = commentsList.find_all(class_="text")
	

		for index, comment in enumerate(comments):
			if comment.find(class_ = "sign") is not None:
				comment.find(class_ = "sign").decompose()
				comment.find(class_ = "title").decompose()
				comment.find(class_ = "answers").decompose()
				payload = {}
				com = comment.get_text(strip=True)
				com = com.replace('\\', '')
				com = remove_smart_quotes(com)
				com = com.strip('\\')
				#comment = comment.replace(\t', '')
				payload["meaning"] = com
				outputList.append(payload)
				
					
		# for index, nu in enumerate(outputList):
		# 	print(index)
		if len(outputList) != 0:
			lyricsTag = soup.find(class_ = "holder lyric-box")
			for a in lyricsTag.find_all("a"):
				a.decompose()
			lyric = lyricsTag.get_text()
			lyric = lyric.replace('\t', '')
			newData = {}
			newData["meaning"] = lyric
			outputList.append(newData)
			print(lyric)
		

		if len(outputList) == 0:
			return getFromGenius(search_query)
		return outputList
	elif target_url is None:
		return getFromGenius(search_query)

		
def getLyrics(soup):
	lyricsTag = soup.find(class_ = "holder lyric-box")
	lyricsTag.find(class_= "editbutton").decompose()
	print(lyricsTag.get_text)



def getFromSongFacts(search_query):
	target_url = startcrawl.findSongFact(search_query)
	response = requests.get(target_url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")
	factlist = soup.find(class_= "factsullist-sf clearfix")
	#print(factlist.prettify())
	songfact = []
	chunks = factlist.find_all("li")

	payload = {}
	payload["meaning"] = ""
	for chunk in chunks:
		text = chunk.contents[0]
		for br in text.find_all("br"):
			br.replace_with("\n")
		com = text.get_text(strip=True)
		payload["meaning"] += " " + com
	songfact.append(payload)
	return songfact

def getFromGenius(search_query):
	target_url = startcrawl.fingGeniusSongUrl(search_query)
	response = requests.get(target_url)
	html = response.text
	soup = bs4.BeautifulSoup(html, "html.parser")

	# for lyric in lyrics:
	# 	data = lyric.get_text()
	# 	print(data)
	content = soup.select(".rich_text_formatting")[0]
	text = content.get_text()
	payload = {}
	data = {}

	payload["meaning"] = text
	songfact = []
	songfact.append(payload)

	lyricsHolder  = soup.find(class_ = "lyrics")
	lyrics = lyricsHolder.find("p").get_text()
	data["meaning"] = lyrics
	songfact.append(data)
	#print(lyrics)
	return songfact
	#for conten in content:
		#print(conten.prettify())

	
if __name__ == '__main__':
	getFromSongsmeanings("Beyoncé Halo")
